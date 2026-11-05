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
- **ICP updated 2026-10-28 (Grok CEO):** owners and CFOs/finance leaders at non-tech companies
  in Canada and the US, with one size band: **under 500 employees by the best headcount signal**.
  Excludes tech companies and consultancies (NAICS exclusion carried over unchanged). Targets
  professional firms and traditional businesses (manufacturing, distribution, retail, logistics,
  construction, healthcare clinics).
- **Buyer titles:** CEO, President, Owner, COO, VP Operations, VP Finance, CFO, with existing title
  aliases retained. French titles include PDG, president, proprietaire, directeur financier,
  VP finances, plus the existing operations and finance equivalents.
- **Search eligibility:** Apollo `estimated_num_employees` >= 30, or **15-29 Apollo employees with
  revenue >= $10M** for field-worker industries that LinkedIn/Apollo undercount. Search the main
  band with `organization_num_employees_ranges: ["30,499"]` and the undercount entry with
  `["15,29"]` plus `revenue_range: {"min": 10000000}`. These are two search entries into the same
  under-500 ICP, with no secondary size band.
- **Best headcount signal:** `max(Apollo estimated_num_employees, revenue-band headcount estimate,
  any stored registry employee count)`, using available headcount signals. Revenue must be translated
  to a supported headcount estimate, never compared as dollars to employees. If no revenue-derived
  estimate is stored or supported, treat that signal as unknown, not as evidence of a small workforce.
  **Reject for upper size only when best signal >= 500**, including exactly 500. A low Apollo count
  cannot override a larger revenue-derived or registry count. The $10M undercount threshold alone
  establishes search eligibility, not the final headcount. Do not use a separate revenue ceiling as
  an upper-size rejection rule.
- Nothing sends to these leads yet. A cold send to a real person is JP's gate.

Never use em-dashes.
