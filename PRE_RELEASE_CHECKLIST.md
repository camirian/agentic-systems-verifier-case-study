# Pre-Release Checklist

- [x] README describes the repository as a public-safe case study.
- [x] Private implementation, datasets, credentials, and build logs are excluded.
- [x] Public claims avoid production, compliance, certification, and replacement-of-review language.
- [x] Public links are intentional.
- [x] Public-export gate (`python3 scripts/verify_public.py`) has been run before release.

## Evidence for the 2026-09-27 Documentation Revision

- `python3 scripts/verify_public.py`: PASS; 13 recognized text files scanned,
  relative Markdown links resolved, and no configured credential-pattern hits.
- Repo Preflight Drift Scanner, `public-export --paranoid`: READY.
- Repo Verification Forge public-surface audit: PASS; 0 findings.
- `gitleaks detect --no-git --redact`: no leaks found.
- Manual review: the README and case study label the workflow and reported
  behavior as conceptual or historical-unverified; no implementation, dataset,
  demo, run logs, or scores are included. Related public links are intentional.

The local verifier does not scan `.env` files, binary files, external links, or
all possible secret formats. The manual boundary review remains required for
those surfaces. This record describes checks for this documentation revision;
it is not approval for a future demo, artifact export, or broader publication.
