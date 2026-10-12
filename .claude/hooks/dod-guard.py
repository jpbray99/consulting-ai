#!/usr/bin/env python3
"""
Definition-of-Done guard. Portfolio-wide.

Turns the "update ROADMAP + memory or you are not done" rule in CLAUDE.md from a
guardrail into a mechanism. The rule asks the agent to remember. This does not ask.

Origin: 2026-07-15. The rule sat in every company's CLAUDE.md for weeks and memory
still rotted, because nothing ever checked. An agent that skipped it and one that did
it got identical outcomes. The 2026-07-05 weekly retro reached the same conclusion on
its own: "A prompt-level rule is not a control ... the fix is mechanical, not textual."
First proposed 2026-06-22 as "Keys, not prompts" and deferred twice.

Self-locating: derives its company from its own path, so this file is byte-identical
in every company and can be copied without edits.
  <COMPANY>/.claude/hooks/dod-guard.py  ->  project = <COMPANY>
                                            memory  = ~/.claude/projects/<slug>/memory

Two modes, wired to two hook events:

  record  (PostToolUse on Edit|Write|NotebookEdit)
          Appends each touched file path to a per-session ledger in $TMPDIR.
          Per session, not `git status`: trees here are routinely dirty with other
          sessions' work (HelionAI carries ~29 such files), and a guard that fires on
          someone else's mess gets muted within a week.

  check   (Stop)
          Reads the ledger. If this session changed substantive project files but wrote
          nothing to ROADMAP.md or the company memory dir, it blocks and says so.

Requires EITHER the roadmap OR memory, never both. Demanding a memory write every
session would train agents to emit one junk memory per sprint to clear the gate, which
is worse than the rot it replaces.

Fails open on every internal error. A broken guard must never brick a session.

2026-09-22 -- TWO BLIND SPOTS FIXED, found when this guard blocked the nightly sprint five
times in a row on a session that had already written and pushed three memory files.

  1. `record` only fires on Edit|Write|NotebookEdit. Sessions running under bypass-permissions
     are instructed to make file changes with Bash (heredocs, sed), so every satisfying write
     they make is invisible to the ledger, while any tool-based write by a SUBAGENT still loads
     the numerator. The guard could only be satisfied by a working style the session was told
     not to use. `check` now also accepts evidence from the filesystem: a memory file modified
     since the ledger was created counts, however it was written.

  2. Satisfaction was hard-scoped to the guard's OWN project root: the portfolio-root
     ROADMAP.md (which does not exist) or the portfolio memory dir. At the portfolio root the
     work is done by company subagents, so `HelionAI/ROADMAP.md`, `Slipstream/memory/MEMORY.md`
     and `LeapVision/FrameFlow/memory/MEMORY.md` all counted as unmet substantive change while
     being exactly the Definition of Done being demanded. Any ROADMAP.md, and any path inside
     any memory/ dir, now satisfies.

An unsatisfiable control is worse than no control: it trains every agent to treat the block as
noise and route around it, which is how a real red one gets ignored later.
"""
import json
import os
import sys
import tempfile

# <PROJECT>/.claude/hooks/dod-guard.py -> up three levels is the project root.
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROADMAP = os.path.join(PROJECT_DIR, "ROADMAP.md")
MEMORY_DIR = os.path.join(
    os.path.expanduser("~/.claude/projects"),
    PROJECT_DIR.replace(os.sep, "-"),
    "memory",
)


def ledger_path(session_id):
    safe = "".join(c for c in str(session_id or "unknown") if c.isalnum() or c in "-_")
    tag = os.path.basename(PROJECT_DIR)
    return os.path.join(tempfile.gettempdir(), "claude-dod-%s-%s.txt" % (tag, safe))


def norm(p):
    try:
        return os.path.realpath(os.path.abspath(p))
    except Exception:
        return p


def under(path, directory):
    try:
        return os.path.commonpath([norm(path), norm(directory)]) == norm(directory)
    except Exception:
        return False


def do_record(payload):
    fp = (payload.get("tool_input") or {}).get("file_path")
    if not fp:
        return
    with open(ledger_path(payload.get("session_id")), "a") as fh:
        fh.write(norm(fp) + "\n")


def do_check(payload):
    # Already blocked once this turn. Blocking again is how you build an infinite loop.
    if payload.get("stop_hook_active"):
        return

    path = ledger_path(payload.get("session_id"))
    if not os.path.exists(path):
        return

    with open(path) as fh:
        touched = [ln.strip() for ln in fh if ln.strip()]
    if not touched:
        return

    if any(p == norm(ROADMAP) for p in touched):
        return
    if any(under(p, MEMORY_DIR) for p in touched):
        return

    # Any ROADMAP.md, not only this project's own: at the portfolio root the roadmaps
    # that actually get updated belong to the companies, written by subagents.
    if any(os.path.basename(p) == "ROADMAP.md" for p in touched):
        return

    # Any path inside a memory/ dir, for the same reason.
    if any("memory" in p.split(os.sep) for p in touched):
        return

    # Bash-written memory is invisible to the ledger. Trust the filesystem instead:
    # anything in the memory dir modified since this session started counts.
    try:
        started = os.stat(path).st_birthtime
        for root, _dirs, files in os.walk(MEMORY_DIR):
            for fn in files:
                if os.stat(os.path.join(root, fn)).st_mtime >= started:
                    return
    except Exception:
        pass

    substantive = sorted(
        {p for p in touched if under(p, PROJECT_DIR) and p != norm(ROADMAP)}
    )
    if not substantive:
        return

    company = os.path.basename(PROJECT_DIR)
    shown = [os.path.relpath(p, PROJECT_DIR) for p in substantive[:8]]
    more = len(substantive) - len(shown)
    listing = "\n".join("  - " + s for s in shown)
    if more > 0:
        listing += "\n  - ...and %d more" % more

    reason = (
        "Definition of Done not met. This session changed %d file(s) under %s but wrote "
        "nothing to ROADMAP.md or the company memory dir:\n\n%s\n\n"
        "Before finishing, do whichever genuinely apply:\n"
        "  1. Update %s -- move the item to Done with today's date, refresh Status / Now "
        "/ Next, and delete any blocker this work resolved (do not label it RESOLVED and "
        "leave it; a stale blocker hides the real ones).\n"
        "  2. If anything material changed (launch state, a live URL, a blocker opened or "
        "cleared, a key decision, a service wired), write it to %s and add its one-line "
        "entry to that dir's MEMORY.md index.\n\n"
        "If a memory you read while working turned out to be WRONG, fix or delete it. Do "
        "not just append a new one beside it. A stale line in MEMORY.md loads into every "
        "future session and outvotes the truth.\n\n"
        "If this session genuinely produced nothing worth recording (a spike, an abandoned "
        "attempt, pure exploration), say so in one line and stop again."
    ) % (len(substantive), company, listing, ROADMAP, MEMORY_DIR)

    print(json.dumps({"decision": "block", "reason": reason}))


def main():
    try:
        mode = sys.argv[1] if len(sys.argv) > 1 else ""
        payload = json.loads(sys.stdin.read() or "{}")
        if mode == "record":
            do_record(payload)
        elif mode == "check":
            do_check(payload)
    except Exception:
        # Fail open, always. Never let this guard be the reason a session dies.
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
