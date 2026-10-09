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
- ICP: CEO, President, Owner, COO, VP Operations at companies with 60-1,000 employees in Canada and
  the US. Targets professional firms and traditional businesses (manufacturing, distribution, retail,
  logistics, construction). Excludes tech companies and consultancies. A second lane covers
  traditional businesses that LinkedIn undercounts (15-59 employees on Apollo, $10M+ revenue).
- Nothing sends to these leads yet. A cold send to a real person is JP's gate.

Never use em-dashes.
