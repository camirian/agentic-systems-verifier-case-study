# CLAUDE.md

Guidance for AI agents and contributors working in this repository.

## What this repo is

This is a **documentation-only public case study** for an agentic systems
verification workflow (systems-engineering review + model-based architecture
review + retrieval-augmented evaluation). It is a sanitized portfolio artifact,
**not** a runnable product. Source of truth: `README.md:3-5`.

There is intentionally **no production source code, no datasets, no copied
standards material, no grant material, no cloud deployment files, no
credentials, and no build logs** in this repo (`README.md:5`,
`docs/RELEASE_BOUNDARY.md:5-13`).

## Repository map

- `README.md` — public landing page: problem, architecture pattern, demonstrated
  behavior, primary user, verification path, exclusions, related public work.
- `SPEC.md` — goal, non-goals, public boundary, success criteria.
- `docs/CASE_STUDY.md` — narrative workflow (normalize → extract → retrieve →
  bounded model assessment → score → human review) and engineering lessons.
- `docs/RELEASE_BOUNDARY.md` — explicit excluded vs included material.
- `MASTER_PLAN.md` — earlier committed master plan (kept for history).
- `docs/MASTER_PLAN.md` — **canonical** master plan going forward (12 sections).
- `VERIFICATION_PLAN.md` — pre-publish checks (automated gate + manual review).
- `PRE_RELEASE_CHECKLIST.md` — release sign-off checklist.
- `SECURITY.md` — public data boundary and private reporting policy.
- `AGENTS.md` — agent rules (read this first; see below).
- `LICENSE` — all rights reserved; published for portfolio review only.
- `.github/dependabot.yml` — weekly github-actions update checks.
- `.gitignore` — ignores `.env*`, caches, build/dist, `node_modules`, `*.log`.

## Agent rules (from `AGENTS.md` — authoritative)

- Keep all examples **synthetic and public-safe**.
- Do **not** add private repo names, customer data, strategy notes, secrets, or
  operational credentials.
- Keep claims **bounded to the public case-study evidence in this repo**.
- **Verify README links and release-boundary docs after changes.**

## Claim discipline (critical)

Public language must stay **case-study / pattern / demonstrated / decision-support**
wording. Do **not** add production-readiness, compliance, certification, safety,
or "replaces human review" claims (`SPEC.md:9-11`, `PRE_RELEASE_CHECKLIST.md:5`).
Every capability claim must map to evidence already in this repo.

## Verification

The documented pre-publish gate (`VERIFICATION_PLAN.md`) historically referenced
`python3 repo_preflight.py --repo . --profile public-export --paranoid`. That
tool is **not present in this repo**. A self-contained, stdlib-only local check
lives at `scripts/verify_public.py` and is the runnable verification path:

```bash
python3 scripts/verify_public.py
```

It resolves internal markdown links / file references and scans for forbidden
patterns (`.env`, credentials, API keys). It exits non-zero on failure. Run it
after any doc change, then complete the manual boundary review in
`VERIFICATION_PLAN.md` and `PRE_RELEASE_CHECKLIST.md` before publishing.

## Conventions

- Markdown only (plus the one stdlib Python verification script). No third-party
  dependencies.
- Keep commits small and reviewable; never `git add -A` (the parent folder is
  non-git). Stage only files you create or edit.
- Never commit secrets, `.env`, private references, or generated logs/reports.
- Branch for any change; never commit directly to `main`.
