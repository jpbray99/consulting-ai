# Consulting AI (working name: Tailored AI)

AI consulting for established, non-tech SMEs: move them past "ask ChatGPT a question" to tailored
workflows, custom in-house apps, software cost review, and team adoption. Moved out of
`LeapVision/consulting-site` on 2026-10-09 (JP): it is its own business, not a LeapVision product.

## Website
- Static site in `dist/`. Brand and copy rules: `brand-spec.md`. Browser QA log: `QA.md`.
- Hosted on GitHub Pages: every push to main deploys `dist/` via `.github/workflows/pages.yml`. OpenAI Sites dropped 2026-10-09 (JP).
- Repo: `jpbray99/consulting-ai` (public, because Pages on the free plan requires it; keep secrets out). Commit and push to main after every change.
- The contact form only builds a copyable brief and sends nothing until a business email or
  booking link is connected.
- The Cartier/Skechers logos refer to past work done through LeapVision. Never present them as
  consulting clients, and never present the illustrative savings as real client results.

## Pipeline
- CRM brand `consulting-ai`, source `consulting-ai-sdr`. Leads come from the nightly
  `portfolio-crm-prospecting` job (section 8 holds the ICP).
- **ICP updated 2026-10-25 (JP):** primary target is now CEO, President, Owner, COO, VP Operations,
  **VP Finance, CFO** (new title track, added 2026-10-25) at companies with **30-300 employees**
  (new primary band) in Canada and the US. Ideally not tech companies -- excludes tech companies and
  consultancies (NAICS exclusion carried over unchanged). Targets professional firms and traditional
  businesses (manufacturing, distribution, retail, logistics, construction, healthcare clinics).
  The old 60-1,000 lane and the 15-59-employee/$10M-revenue undercount lane stay as secondary lanes
  (still valid, lower priority) -- see section 8 for the full lane breakdown.
- As of 2026-10-25 the CRM already holds 1,048 consulting-ai contacts from the nightly job
  (2026-10-09 to date); 673 of those already sit at companies in the new 30-300 band. The CFO/VP
  Finance track was essentially never pulled before (2 incidental hits out of 1,048).
- Nothing sends to these leads yet. A cold send to a real person is JP's gate.

Never use em-dashes.
