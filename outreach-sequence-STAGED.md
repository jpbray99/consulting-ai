# Consulting AI Outreach - STAGED - do not activate

Staged 2026-10-25. Target audience: CEO, COO, VP Operations, VP Finance, CFO at 30-300 employee
non-tech SMEs (new ICP, see CLAUDE.md Pipeline + the SDR skill's section 8). Positioning per
brand-spec.md: "You've tried AI. Now put it to work."

**Not created as a live Instantly campaign object.** Instantly's `create_campaign` API hard-requires
a real sender mailbox to be assigned before it will create the campaign at all (confirmed 2026-10-25:
it offered only Biomi's and Movemint's existing mailboxes as "eligible senders," there is no
consulting-ai or Tailored AI sender). Assigning this content to another brand's live mailbox would
send Consulting AI copy from a Biomi or Movemint domain, which is a cross-brand misattribution, not a
harmless staging step, so it was not done. This file is the ready-to-paste draft: the moment a
consulting-ai sender mailbox exists, create the Instantly campaign with this exact name and paste in
the 4 steps below with the cadence given.

Cadence: Day 0, Day 4, Day 9 (5-day gap), Day 15 (6-day gap). Stop on reply, stop on auto-reply.
Daily limit 30/sender, 15 min gap between sends.

## Step 1 (Day 0)
**Subject:** Quick question about AI at {{companyName}}

Hi {{firstName}},

Most operators I talk with have tried AI in bits and pieces: a ChatGPT session here, a draft email
there. Few have it actually built into a specific workflow.

Curious where {{companyName}} sits on that. Worth a short call to compare notes?

Best,
JP

## Step 2 (Day 4)
**Subject:** What "built in" looks like

Hi {{firstName}},

Following up briefly. The difference that matters for a 30-300 person operation isn't using AI, it's
having one workflow (reporting, intake, scheduling, vendor comparison) rebuilt around it, so a task
that used to take hours takes a fraction of that, every week, without anyone having to remember to
use it.

We do the opposite of a generic AI course: we look at one real workflow in your operation, cost it
out, and rebuild it.

Happy to walk through what that would look like for {{companyName}} if useful.

Best,
JP

## Step 3 (Day 9)
**Subject:** A 20-minute AI audit for {{companyName}}

Hi {{firstName}},

Last note from me on this one. If it's useful, we offer a short, no-obligation review: one call, we
look at two or three of your team's repetitive tasks, and tell you plainly which ones are worth
automating now and which aren't.

No deck, no sales pitch, just a straight read on where the time is going.

Open to 20 minutes this week or next?

Best,
JP

## Step 4 (Day 15, breakup)
**Subject:** Closing the loop

Hi {{firstName}},

I'll leave it here for now. If putting AI to work in {{companyName}}'s operations becomes a priority
later this year, happy to pick this back up, just reply.

All the best,
JP

## Setup checklist for when a sender exists
1. Buy/connect a consulting-ai or Tailored AI domain mailbox (JP's call -- money leaving an account).
2. `create_campaign` with this name, these 4 steps, `email_list` set to that new sender.
3. Pull the qualified CRM contacts (`brand=consulting-ai`) into an Instantly lead list.
4. Warm the mailbox before activating -- do not launch cold.
5. The send button itself is still JP's gate per the portfolio autonomy rule even once staged.
