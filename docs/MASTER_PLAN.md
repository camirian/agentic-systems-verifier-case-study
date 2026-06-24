# Master Plan: Agentic Systems Verifier Case Study

> **Canonical copy.** A root `MASTER_PLAN.md` was committed earlier
> (commit `03d2dda`) and is retained for history. This file
> (`docs/MASTER_PLAN.md`) is the canonical master plan going forward. Where the
> two differ, this file wins. Section 12 and the verification references here
> reflect the now-runnable local check at `scripts/verify_public.py`.

Each item below is tagged **Facts** (repo evidence), **Assumptions**, or
**Recommendations**.

## 1. Executive Summary

### Facts

- This repository is a public case study for an agentic systems verification
  workflow that combines systems-engineering review, model-based architecture
  review, and retrieval-augmented evaluation. Evidence: `README.md:3`.
- The repository intentionally excludes production source code, datasets, copied
  standards material, grant material, cloud deployment files, credentials, and
  build logs. Evidence: `README.md:5`, `docs/RELEASE_BOUNDARY.md:5-13`.
- The public artifact is documentation plus a public demo link, not an
  implementation dump. Evidence: `README.md:38`, `docs/CASE_STUDY.md:36`.
- The primary user is a technical reviewer, systems engineer, or portfolio
  reviewer evaluating whether the workflow shape preserves evidence visibility
  and the public-release boundary. Evidence: `README.md:50`.

### Assumptions

- Any private implementation remains outside this public candidate and must not
  be imported without a separate public-surface audit.
- The current release goal is a safe, credible public portfolio artifact, not a
  runnable verifier product.
- The referenced public demo remains intentionally public and approved.

### Recommendations

- Treat this repo as a bounded public case-study product: "ready" means
  claim-accurate, sanitized, link-verified documentation with clear non-goals.
- Do not add verifier source code until there is a separate public export
  boundary, dependency review, synthetic fixtures, and reproducible tests.
- Make the next implementation slice a release-boundary / verification hardening
  pass, not a feature build.

## 2. Current-State Findings (with file/path evidence)

### Facts

- `AGENTS.md` requires synthetic, public-safe examples, bounded claims, and
  verification of README links and release-boundary docs after changes.
  Evidence: `AGENTS.md:5-9`.
- `README.md` describes the problem, architecture pattern, demonstrated
  behavior, public user, verification path, exclusions, public artifacts, and
  related public work. Evidence: `README.md:16,28,40,48,52,56,65,70`.
- `SPEC.md` defines the goal as documenting a public-safe case study and
  excludes original source code, private datasets, copied standards material,
  provider configuration, internal planning notes, private prompts, credentials,
  and machine-specific setup. Evidence: `SPEC.md:5,9-11`.
- `docs/CASE_STUDY.md` defines the workflow as normalization, extraction,
  retrieval, bounded model assessment, scoring, and human review. Evidence:
  `docs/CASE_STUDY.md:11-16`.
- `docs/RELEASE_BOUNDARY.md` lists excluded and included material. Evidence:
  `docs/RELEASE_BOUNDARY.md:5-13,15-21`.
- `VERIFICATION_PLAN.md` documents a public-export gate plus manual checks.
  Evidence: `VERIFICATION_PLAN.md:5,11-15`.
- `SECURITY.md` forbids real secrets, customer data, private repo content,
  operational credentials, private keys, API tokens, `.env` contents, and
  machine-specific network identifiers. Evidence: `SECURITY.md:3-5,15-16`.
- Recent git history shows public hardening and DORA user-verification work:
  `Add public repository guardrails`, `Add DORA user verification path`,
  `Tighten public repo landing copy`, `docs: add master plan`. Evidence:
  `git log --oneline`.

### Assumptions

- The checked-in docs are the intended public source; any private
  implementation evidence stays outside this repo.

### Facts (verification gap, confirmed)

- The previously documented entry point `repo_preflight.py` is **not present**
  in this repo or its parent directory (verified by filesystem search). The
  release verification path was therefore not self-contained.

### Recommendations

- Provide a self-contained, stdlib-only verification command (done in the first
  slice: `scripts/verify_public.py`) and repoint `VERIFICATION_PLAN.md` and
  `PRE_RELEASE_CHECKLIST.md` at it.
- Keep future claims bounded to case-study / pattern / demonstrated /
  decision-support wording.
- Record release evidence after each public update: files changed, links
  checked, verification result, manual boundary review, remaining risk.

## 3. Product Requirements

### Facts

- Target users are technical reviewers, systems engineers, and portfolio
  reviewers. Evidence: `README.md:50`.
- The case study must explain the problem, architecture pattern, demonstrated
  behavior, and excluded material. Evidence: `SPEC.md:19-21`.
- Public artifacts are `docs/CASE_STUDY.md` and `docs/RELEASE_BOUNDARY.md`.
  Evidence: `README.md:67-68`.

### Assumptions

- Reviewers need enough detail to judge engineering quality without private
  corpora, code, prompts, provider settings, or logs.
- The repo should stay useful even if the demo video becomes unavailable.

### Recommendations

- **Primary workflows:** reviewer reads `README.md` → `docs/CASE_STUDY.md` →
  `docs/RELEASE_BOUNDARY.md`; maintainer updates claims and runs the
  public-export gate; maintainer records release evidence before publishing.
- **Non-goals:** runnable verifier product; release of private source, datasets,
  standards PDFs, prompts, cloud config, credentials, or logs; compliance /
  safety / certification / autonomy claims.
- **Required features:** public-safe overview; architecture-pattern explanation;
  human-review role; explicit excluded-material boundary; link/claim
  verification; public-export provenance notes for future private syncs.
- **Error / recovery states:** broken public link → block release until fixed or
  removed; missing preflight tool → record substitute and block readiness claim;
  private material detected → remove before release, audit history.
- **Data handling:** no private/customer data, prompts, provider config, copied
  standards, datasets, or logs; only public-safe narrative docs and approved
  links.
- **Security / boundary:** default-deny secrets, credentials, `.env`, private
  repo content, customer data, machine identifiers, internal notes.

## 4. DORA AI Capability Alignment

### Facts

- The case study presents an AI-assisted workflow where model output is a review
  candidate and humans stay in the loop. Evidence: `docs/CASE_STUDY.md:7,16,21`.
- The repo currently contains documentation, not an AI system implementation.
  Evidence: `README.md:5`.

### Assumptions

- DORA alignment here describes how this public artifact would support
  AI-enabled delivery discipline if implementation code is later exported.

### Recommendations

- **AI stance:** allow public-safe explanation, synthetic examples, diagrams;
  restrict prompts, eval code, provider settings, traces pending separate
  review; prohibit private corpora, copied standards, customer data, grant
  content, secrets, credentials.
- **Data ecosystem:** maintain a source register (owner, freshness, approval)
  for public docs, demo links, and any future synthetic fixtures.
- **AI-accessible internal data:** agents may use only this repo's public docs,
  approved synthetic examples, and public links.
- **Version control:** small reviewable commits; preserve generated-vs-source
  boundaries; require public-surface review for any synced material.
- **Small batches:** first useful slice is a self-contained verification + claim
  audit, not a feature build.
- **User-centricity:** named user = technical reviewer; JTBD = understand the
  verifier pattern and release boundary without private context; success signal
  = reviewer distinguishes demonstrated behavior from excluded implementation.
- **Internal platform:** provide one documented path for public-export preflight
  — now satisfied by `scripts/verify_public.py`.
- **Closed DORA gap:** a self-contained, runnable public-export command now
  exists in this repo (was previously missing).

## 5. Architecture Plan

### Facts

- Existing architecture is a documentation-only release surface: `README.md`,
  `SPEC.md`, `VERIFICATION_PLAN.md`, `PRE_RELEASE_CHECKLIST.md`, `SECURITY.md`,
  and `docs/`.
- The described verifier pattern has ingestion, parsing, retrieval,
  verification, and review-UI layers. Evidence: `README.md:32-36`.

### Assumptions

- Any future runnable architecture must use synthetic/public fixtures and must
  not depend on private corpora.

### Recommendations

- **Existing:** root docs define framing, spec, verification, checklist, and
  security; `docs/CASE_STUDY.md` carries the narrative; `docs/RELEASE_BOUNDARY.md`
  carries the boundary.
- **Proposed public layout:** `docs/` source-of-truth narrative; `scripts/`
  public-surface and link checks (introduced this slice); optional `examples/`
  synthetic fixtures only; optional `release/` generated reports, ignored unless
  intentionally published.
- **Future runnable demo data flow:** synthetic source → parser → retriever →
  bounded evaluator → evidence-linked review report.
- **Config / secrets:** no `.env`, tokens, provider configs, customer material,
  machine-specific paths, or private references.
- **ADR needs:** documentation-only vs runnable sanitized demo; public synthetic
  evaluation fixture policy.

## 6. Feature Roadmap (milestones with acceptance criteria)

### Recommendations

- **M1 — Public-readiness hardening.** Acceptance: all internal links resolve,
  the preflight path is executable or explicitly external, claims map to
  evidence. (Substantially delivered this slice.)
- **M2 — Claim taxonomy.** Acceptance: docs distinguish demonstrated, public
  inference, planned, and excluded claims.
- **M3 — Release evidence template.** Acceptance: maintainers can record
  verification result, manual audit, link checks, artifact-boundary check, and
  remaining risk per release.
- **M4 — Optional synthetic mini-fixture.** Acceptance: any example uses invented
  data only and does not imply production readiness.
- **M5 — Public artifact packaging.** Acceptance: a generated archive contains
  only public docs, license, security policy, and approved public assets.

## 7. Parallelization Plan

### Recommendations

- **Workstream A — Claim & link audit.** Owns `README.md`, `docs/CASE_STUDY.md`.
  Verify via link check + claim-evidence table.
- **Workstream B — Release-boundary audit.** Owns `docs/RELEASE_BOUNDARY.md`,
  `SECURITY.md`, `PRE_RELEASE_CHECKLIST.md`. Verify via public-surface scan +
  excluded-material checklist.
- **Workstream C — Verification tooling.** Owns `scripts/`, `VERIFICATION_PLAN.md`.
  Verify via one-command public preflight.
- **Workstream D — Optional synthetic example.** Owns future `examples/`. Verify
  fixture is synthetic and cannot reveal private provenance.
- **Sequential gate:** public publication waits for all workstreams plus
  public-surface, artifact-boundary, and claim review.
- **Merge strategy:** small PRs per workstream; update the release checklist only
  after integration.

## 8. Task Backlog

### Recommendations

| Priority | Task | Likely files | Tests/docs | Verification | Done condition |
| --- | --- | --- | --- | --- | --- |
| P0 | Replace missing preflight entry point | `scripts/verify_public.py`, `VERIFICATION_PLAN.md`, `PRE_RELEASE_CHECKLIST.md` | Update verification docs | `python3 scripts/verify_public.py` | Public verifier command is runnable in-repo (**done this slice**) |
| P0 | Internal-link / file-reference audit | `README.md`, `docs/*.md` | Fix links if needed | `scripts/verify_public.py` link resolver | No broken internal links |
| P0 | Claim-evidence matrix | `README.md`, `docs/CASE_STUDY.md` | Add table/checklist | Manual review | Every claim maps to evidence or is downgraded |
| P0 | Release evidence template | `PRE_RELEASE_CHECKLIST.md` / `docs/RELEASE_BOUNDARY.md` | Checklist update | Manual review | Release decision is replayable |
| P1 | Generated-vs-source policy | `docs/RELEASE_BOUNDARY.md` | Boundary docs | Manual inspection | Generated reports/logs excluded unless approved |
| P1 | Synthetic-fixture policy | `SPEC.md` | Spec update | Public-boundary review | Future examples cannot use private data |
| P1 | Artifact package check | future `scripts/` | Script docs | Extract archive + scan manifest | Packaged artifact contains only approved files |
| P2 | Narrative diagram | `docs/CASE_STUDY.md` | Public-safe diagram | Render check | Diagram explains layers without leakage |

## 9. Testing & Verification Plan

### Facts

- The repo is documentation-only plus one stdlib verification script. Evidence:
  `README.md:54`.
- Release verification is a public-export gate plus manual checks. Evidence:
  `VERIFICATION_PLAN.md:5,11-15`.

### Assumptions

- Unit/integration tests are not applicable until code or fixtures are added.

### Recommendations

- **Automated (runnable now):** `python3 scripts/verify_public.py` resolves
  internal markdown links and scans for forbidden patterns; exits non-zero on
  failure.
- **Documentation checks:** verify internal links, file references, and that
  excluded-material wording remains present.
- **Public-surface audit:** scan for `.env`, credentials, tokens, customer data,
  copied standards, grant material, and build logs.
- **Artifact-boundary checks:** if packaging, list the manifest, extract to a
  temp dir, scan contents, confirm only reviewer-useful files are included.
- **Claim accuracy:** maintain a claim table with source-line evidence.
- **Regression loop after any doc change:** run `verify_public.py` → public-
  surface scan → claim review → release checklist update.

## 10. Release Criteria

### Facts

- `PRE_RELEASE_CHECKLIST.md` marks public-safe README, excluded private
  materials, bounded claims, intentional public links, and the public-export
  gate as checked. Evidence: `PRE_RELEASE_CHECKLIST.md:3-7`.

### Recommendations

- **Definition of done:** README, case study, release boundary, spec, security
  policy, and verification plan agree; public claims are backed by repo
  evidence; `python3 scripts/verify_public.py` passes (or any failure is
  recorded as a release blocker).
- **Public-readiness checklist:** no secrets, credentials, private datasets,
  copied standards, prompts, provider configs, build logs, machine-specific
  setup, or customer data; no production/compliance/certification/safety/
  human-replacement claims; public links intentional and reachable.
- **Artifact-boundary checklist:** archive manifest inspected; extracted archive
  scanned; generated logs/reports excluded.
- **Operational handoff:** maintainer can run the verification path without
  private context.

## 11. Risks & Open Questions

### Facts

- The repo intentionally omits implementation code and private evidence, so the
  original verifier behavior cannot be reproduced from this repo alone.

### Risks

- **Claim inflation:** public language may imply production readiness.
- **Verification gap (mitigated):** the prior `repo_preflight.py` reference was
  unavailable; now replaced by an in-repo script.
- **Link rot:** demo and related-repo links may drift.
- **Provenance ambiguity:** future private syncs could copy internal context.
- **Generated-artifact leakage:** preflight/build logs or reports could be
  committed accidentally.

### Open Questions

- Should the repo stay documentation-only permanently, or add a synthetic
  runnable mini-demo?
- Should external public links (demo video, related repos) be checked online by
  the verifier, or remain manual to keep the script offline/stdlib-only?
- Where should release evidence live — repo docs, PR descriptions, or generated
  local reports?

## 12. Recommended First Implementation Slice

### Recommendation

Ship a **self-contained public-release verification script**, then repoint the
documented release gate at it.

### Why it is first

- It directly protects the public-export boundary (the repo's core identity).
- It closes the confirmed gap where `VERIFICATION_PLAN.md` referenced a
  `repo_preflight.py` tool that does not exist in the repo.
- It gives a genuinely runnable verification with captured results, without
  expanding product surface.

### What it changes

- Add `scripts/verify_public.py` (Python stdlib only): resolves every internal
  markdown link and fails on missing targets; scans
  tracked text files for forbidden patterns (`.env` contents, API keys,
  credentials); exits non-zero on any failure.
- Repoint `VERIFICATION_PLAN.md` and `PRE_RELEASE_CHECKLIST.md` from the missing
  `repo_preflight.py` to `python3 scripts/verify_public.py`.
- Document the command in `CLAUDE.md` and `README.md`.

### What it does NOT change

- No verifier implementation code, no private source import, no model-provider
  configuration, no third-party dependencies, no generated reports committed by
  default.

### Acceptance criteria

- `python3 scripts/verify_public.py` runs with the system Python (stdlib only)
  and exits `0` on the current clean repo.
- All internal markdown links resolve.
- The forbidden-pattern scan reports no findings.
- `VERIFICATION_PLAN.md` and `PRE_RELEASE_CHECKLIST.md` reference a command that
  actually exists in the repo.

### Verification path

1. `python3 scripts/verify_public.py` (expect exit 0, all checks pass).
2. `git diff --check` (no whitespace errors).
3. Manual scan for secrets, private references, generated logs, unsupported
   claims.
