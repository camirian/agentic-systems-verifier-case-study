# Master Plan: Agentic Systems Verifier Case Study

## 1. Executive Summary

### Facts

- This repository is a public case study for an agentic systems verification workflow that combines systems engineering review, model-based architecture review, and retrieval-augmented evaluation. Evidence: `README.md:3`.
- The repository intentionally excludes production source code, datasets, copied standards material, grant material, cloud deployment files, credentials, and build logs. Evidence: `README.md:5`, `docs/RELEASE_BOUNDARY.md:5`.
- The public artifact is documentation plus a public demo link, not an implementation dump. Evidence: `README.md:38`, `docs/CASE_STUDY.md:36`.
- The primary user is a technical reviewer, systems engineer, or portfolio reviewer evaluating whether the workflow shape preserves evidence visibility and public-release boundaries. Evidence: `README.md:50`.

### Assumptions

- The private implementation, if any, remains outside this public candidate and must not be imported into this repo without a separate public-surface audit.
- The current release goal is a safe, credible public portfolio artifact rather than a runnable verifier product.
- The referenced public demo remains intentionally public and approved for inclusion.

### Recommendations

- Treat this repo as a bounded public case-study product: its "ready" state is claim-accurate, sanitized, link-verified documentation with clear non-goals.
- Do not add verifier source code until the project has a separate public export boundary, dependency review, synthetic fixtures, and reproducible tests.
- Make the next implementation slice a documentation-quality and release-boundary hardening pass, not a feature build.

## 2. Current-State Findings, With File/Path Evidence

### Facts

- `AGENTS.md` is present and requires synthetic, public-safe examples, bounded claims, and verification of README links and release-boundary docs after changes. Evidence: `AGENTS.md:1`, `AGENTS.md:5`.
- `README.md` describes the problem, architecture pattern, demonstrated behavior, public user, verification path, exclusions, public artifacts, and related public work. Evidence: `README.md:16`, `README.md:31`, `README.md:45`, `README.md:50`, `README.md:54`, `README.md:64`.
- `SPEC.md` defines the goal as documenting a public-safe case study and explicitly excludes original source code, private datasets, copied standards material, provider configuration, internal planning notes, private prompts, credentials, and machine-specific setup. Evidence: `SPEC.md:5`, `SPEC.md:9`, `SPEC.md:11`.
- `docs/CASE_STUDY.md` defines the workflow as normalization, extraction, retrieval, bounded model assessment, scoring, and human review. Evidence: `docs/CASE_STUDY.md:11`.
- `docs/RELEASE_BOUNDARY.md` lists excluded and included material. Evidence: `docs/RELEASE_BOUNDARY.md:5`, `docs/RELEASE_BOUNDARY.md:17`.
- `VERIFICATION_PLAN.md` requires `python3 repo_preflight.py --repo . --profile public-export --paranoid` and manual checks before release. Evidence: `VERIFICATION_PLAN.md:5`, `VERIFICATION_PLAN.md:11`.
- `SECURITY.md` warns not to include real secrets, customer data, private repo content, operational credentials, private keys, API tokens, `.env` contents, customer data, or machine-specific network identifiers. Evidence: `SECURITY.md:3`, `SECURITY.md:15`.
- Recent git history shows public hardening and DORA user-verification work, including `Add public repository guardrails`, `Add DORA user verification path`, and `Tighten public repo landing copy`.

### Assumptions

- `repo_preflight.py` may be supplied by an external workspace tool rather than committed in this candidate repo.
- The current checked-in docs are the intended public source, while any private implementation evidence stays outside this repo.

### Recommendations

- Add or document the exact location of `repo_preflight.py`; otherwise, the release verification path is not self-contained.
- Keep future claims as "case study", "pattern", "demonstrated", and "decision support" claims. Avoid production, compliance, safety, certification, or replacement-of-review claims.
- Maintain a small release evidence section after each public update: files changed, links checked, preflight result, manual public-boundary review result, and remaining risk.

## 3. Product Requirements

### Facts

- Target users are technical reviewers, systems engineers, and portfolio reviewers. Evidence: `README.md:50`.
- The case study must explain the problem, architecture pattern, demonstrated behavior, and excluded material. Evidence: `SPEC.md:19`.
- Public artifacts are `docs/CASE_STUDY.md` and `docs/RELEASE_BOUNDARY.md`. Evidence: `README.md:64`.

### Assumptions

- Reviewers need enough detail to evaluate engineering judgment without access to private corpora, implementation code, prompts, provider settings, or logs.
- The repo should remain useful even if the demo video is unavailable, by preserving a complete written description.

### Recommendations

- Primary workflows:
  - Public reviewer reads `README.md`, then `docs/CASE_STUDY.md`, then `docs/RELEASE_BOUNDARY.md`.
  - Maintainer updates case-study claims and runs the public-export gate.
  - Maintainer records release evidence before any public publication.
- Non-goals:
  - Runnable verifier product.
  - Public release of private source, datasets, standards PDFs, prompts, cloud configuration, credentials, or build logs.
  - Compliance, safety, certification, or autonomous decision-making claims.
- Required features:
  - Public-safe overview.
  - Architecture-pattern explanation.
  - Human-review role.
  - Explicit excluded-material boundary.
  - Link and claim verification checklist.
  - Public-export provenance notes for any future sync from private sources.
- Supporting capabilities:
  - Public-surface audit checklist.
  - Artifact-boundary checklist for generated packages or release archives.
  - Claim taxonomy separating demonstrated, inferred, planned, and excluded capability.
- Admin/operator workflows:
  - Maintain release checklist.
  - Verify links.
  - Run or document preflight checks.
  - Keep generated outputs and source docs clearly separated.
- Error and recovery states:
  - Broken public link: mark release blocked until corrected or removed.
  - Missing preflight tool: record substitute checks and block public-readiness claim.
  - Private material detected: remove before release and audit history if anything was public.
- Data handling and retention:
  - No private data, customer data, private prompts, provider configuration, copied standards, datasets, or logs in this repo.
  - Keep only public-safe narrative docs and approved public links.
- Security, privacy, and public/private boundary:
  - Default deny for secrets, credentials, `.env`, private repo content, customer data, machine identifiers, and internal operating notes.

## 4. DORA AI Capability Alignment

### Facts

- The public case study presents an AI-assisted workflow where model output is a review candidate and humans remain in the loop. Evidence: `docs/CASE_STUDY.md:7`, `docs/CASE_STUDY.md:15`.
- The repository currently contains documentation, not an AI system implementation. Evidence: `README.md:5`.

### Assumptions

- DORA alignment should describe how this public artifact would support AI-enabled delivery discipline if implementation code is later exported.

### Recommendations

- AI stance:
  - Allowed: public-safe explanation of AI review patterns, synthetic examples, architecture diagrams, and non-sensitive evaluation concepts.
  - Restricted: model prompts, evaluation code, provider settings, and traces only after a separate public-boundary review.
  - Prohibited: private corpora, copied standards, customer data, grant content, secrets, provider credentials, and generated answers that reveal private source context.
- Data ecosystem:
  - Maintain a source register for public docs, demo links, and any future synthetic fixtures.
  - Record owner, freshness, and public approval for each source.
- AI-accessible internal data:
  - Agents may use only this repo's public docs, approved synthetic examples, and public links.
  - Agents may not use private implementation notes or private strategy as source material for public docs.
- Version control:
  - Keep commits small and reviewable.
  - Preserve generated-vs-source boundaries.
  - Require public-surface review for any synced material from private provenance.
- Small batches:
  - First useful slice: self-contained release verification and claim-audit checklist.
- User-centricity:
  - Named user: technical reviewer.
  - Job-to-be-done: understand the verifier pattern and release boundary without private context.
  - Success signal: reviewer can distinguish demonstrated behavior from excluded implementation.
  - Feedback loop: public issue or review comment tagged as claim clarity, boundary clarity, or missing evidence.
- Internal platform:
  - Provide one command or one documented path for public-export preflight.
  - If `repo_preflight.py` is external, document the external location or add a local wrapper.
- Missing DORA evidence:
  - No self-contained automated public-export command is present in this repo.
  - First action: add a local `make verify-public` or documented equivalent once write scope expands beyond this plan.

## 5. Architecture Plan

### Facts

- Existing architecture is a documentation-only release surface with `README.md`, `SPEC.md`, `VERIFICATION_PLAN.md`, `PRE_RELEASE_CHECKLIST.md`, `SECURITY.md`, and `docs/`.
- The described verifier pattern has ingestion, parsing, retrieval, verification, and review UI layers. Evidence: `README.md:31`.

### Assumptions

- Any future runnable architecture must use synthetic/public fixtures and must not depend on private corpora.

### Recommendations

- Existing architecture:
  - Root docs define public framing, spec, verification, release checklist, and security policy.
  - `docs/CASE_STUDY.md` carries the narrative workflow.
  - `docs/RELEASE_BOUNDARY.md` carries included/excluded boundaries.
- Proposed public architecture:
  - `docs/`: source-of-truth public narrative.
  - `examples/`: optional synthetic fixtures only, if future code is added.
  - `scripts/`: optional public-surface and link checks.
  - `release/`: optional generated audit reports, ignored unless intentionally published.
- Data flow for future runnable demo:
  - Synthetic source artifact -> parser -> retriever -> bounded model/evaluator -> evidence-linked review report.
- External integrations:
  - Public demo video and public related repositories only.
  - Model provider integration is out of scope unless fully synthetic and credential-free.
- Configuration and secrets:
  - No `.env`, tokens, provider configs, customer material, machine-specific paths, or private source references.
- Scalability and maintainability:
  - Keep this repo small; use links to public docs rather than duplicating private implementation detail.
- ADR needs:
  - ADR: documentation-only case study vs runnable sanitized demo.
  - ADR: public synthetic evaluation fixture policy.

## 6. Feature Roadmap

### Facts

- The repo already has the core case-study docs and release-boundary docs.
- The verification command is documented but not self-contained from current repo files.

### Assumptions

- The next goal is public-readiness hardening, not expanding product surface.

### Recommendations

- Milestone 1: Public-readiness hardening.
  - Acceptance: all internal links resolve, preflight path is executable or explicitly external, and claims map to evidence.
- Milestone 2: Claim taxonomy.
  - Acceptance: docs distinguish demonstrated, public inference, planned, and excluded claims.
- Milestone 3: Release evidence template.
  - Acceptance: maintainers can record preflight result, manual audit, link checks, artifact-boundary check, and remaining risk for each release.
- Milestone 4: Optional synthetic mini-fixture.
  - Acceptance: any example uses invented data only and does not imply production readiness.
- Milestone 5: Public artifact packaging.
  - Acceptance: generated archive contains only public docs, license, security policy, and approved public assets.

## 7. Parallelization Plan

### Facts

- Work can be divided by documentation, verification tooling, and release audit without touching private implementation.

### Assumptions

- Multiple agents may work concurrently if file ownership is explicit.

### Recommendations

- Workstream A: Claim and link audit.
  - Owns: `README.md`, `docs/CASE_STUDY.md`.
  - Verification: link check and claim-evidence table.
- Workstream B: Release-boundary audit.
  - Owns: `docs/RELEASE_BOUNDARY.md`, `SECURITY.md`, `PRE_RELEASE_CHECKLIST.md`.
  - Verification: public-surface scan and excluded-material checklist.
- Workstream C: Verification command hardening.
  - Owns: future `Makefile` or `scripts/`.
  - Verification: one-command public preflight.
- Workstream D: Optional synthetic example.
  - Owns: future `examples/`.
  - Verification: fixture contains only synthetic content and cannot reveal private provenance.
- Sequential gates:
  - Public publication must wait for all workstreams, public-surface audit, artifact-boundary audit, and claim review.
- Merge strategy:
  - Prefer small PRs by workstream with release checklist updated only after integration.

## 8. Task Backlog

### Facts

- The current docs already name the public boundary and pre-release checks.

### Recommendations

| Priority | Task | Likely files | Tests/docs | Verification | Done condition |
| --- | --- | --- | --- | --- | --- |
| P0 | Verify or replace missing preflight entry point | `VERIFICATION_PLAN.md`, optional `Makefile` | Update verification docs | `python3 repo_preflight.py --repo . --profile public-export --paranoid` or documented substitute | Public verifier command is runnable or intentionally external |
| P0 | Run internal-link audit | `README.md`, `docs/*.md` | Fix links if needed | Link checker or `rg` plus file existence checks | No broken internal links |
| P0 | Create claim-evidence matrix | `README.md`, `docs/CASE_STUDY.md` | Add table or checklist | Manual review | Every capability claim maps to public evidence or is downgraded |
| P0 | Add release evidence template | `PRE_RELEASE_CHECKLIST.md` or `docs/RELEASE_BOUNDARY.md` | Checklist update | Manual review | Release decision can be replayed |
| P1 | Define generated-vs-source policy | `docs/RELEASE_BOUNDARY.md` | Boundary docs | Manual artifact inspection | Generated reports/logs are excluded unless approved |
| P1 | Add optional public synthetic fixture policy | `SPEC.md` | Spec update | Public-boundary review | Future examples cannot use private data |
| P1 | Add artifact package check | future `scripts/` | Script docs | Extract archive and scan manifest | Packaged artifact contains only approved files |
| P2 | Add optional narrative diagram | `docs/CASE_STUDY.md` | Public-safe diagram | Link/render check | Diagram explains layers without implementation leakage |

## 9. Testing And Verification Plan

### Facts

- This is currently documentation-only. Evidence: `README.md:54`.
- Release verification is a public-export gate plus manual checks. Evidence: `VERIFICATION_PLAN.md:5`, `VERIFICATION_PLAN.md:11`.

### Assumptions

- Unit and integration tests are not applicable until code or fixtures are added.

### Recommendations

- Documentation checks:
  - Check internal links and public demo links.
  - Verify all file references exist.
  - Verify excluded-material wording remains present.
- Public-surface audit:
  - Scan for `.env`, credentials, tokens, private repo names beyond approved private/public boundary explanation, customer data, copied standards, grant material, and build logs.
- Artifact-boundary checks:
  - If packaging, generate archive, list manifest, extract to temp directory, scan extracted contents, and verify only buyer/reviewer-useful files are included.
- Claim accuracy:
  - Maintain a claim table with source line evidence and allowed wording.
- Generated-vs-source role separation:
  - Treat docs as source.
  - Treat release reports, preflight logs, and archives as generated artifacts unless explicitly approved.
- Regression loop:
  - After any doc change: link check -> public-surface scan -> claim review -> release checklist update.

## 10. Release Criteria

### Facts

- `PRE_RELEASE_CHECKLIST.md` currently marks public-safe README, excluded private materials, bounded claims, intentional public links, and public-export gate as checked. Evidence: `PRE_RELEASE_CHECKLIST.md:3`.

### Recommendations

- Definition of done:
  - README, case study, release boundary, spec, security policy, and verification plan agree.
  - Public claims are backed by public repo evidence.
  - Public-export preflight has passed or the missing command is explicitly recorded as a release blocker.
- Public-readiness checklist:
  - No secrets, credentials, private datasets, copied standards, private prompts, provider configs, build logs, machine-specific setup, or customer data.
  - No production, compliance, certification, safety, or human-replacement claims.
  - Public links are intentional and reachable.
- Artifact-boundary checklist:
  - Archive manifest inspected.
  - Extracted archive scanned.
  - Generated logs and local reports excluded.
- Operational handoff:
  - Maintainer can run the verification path without private context.
- Remote preservation:
  - For important releases, preserve via normal GitHub branch/PR workflow only after explicit approval.

## 11. Risks And Open Questions

### Facts

- The repo intentionally omits implementation code and private evidence, so reviewers cannot reproduce the original verifier behavior from this repo alone.

### Risks

- Claim inflation: public language may imply production readiness or full implementation availability.
- Verification gap: documented `repo_preflight.py` may be unavailable inside the repo.
- Link rot: demo and related repo links may drift.
- Provenance ambiguity: future syncs from private work could copy internal planning or operational context.
- Generated artifact leakage: preflight logs, build logs, or generated reports could be accidentally committed.

### Open Questions

- Should the public repo remain documentation-only permanently, or eventually add a synthetic runnable mini-demo?
- Where is the canonical public-export preflight tool located, and should this repo include a wrapper?
- Should release evidence be stored in repo docs, PR descriptions, or generated local reports?

## 12. Recommended First Implementation Slice

### Recommendation

Build a public-release verification slice.

### Why It Is First

- It directly protects the public-export boundary.
- It closes the gap between documented release checks and reproducible release evidence.
- It avoids expanding functionality before the repo can prove claim and artifact safety.

### What It Changes

- Add or document a self-contained verification command.
- Add a claim-evidence checklist.
- Add a release evidence template.
- Confirm link and file-reference integrity.

### What It Does Not Change

- No verifier implementation code.
- No private source import.
- No model-provider configuration.
- No generated reports committed by default.

### Acceptance Criteria

- A fresh reviewer can identify what is included, excluded, demonstrated, and not claimed.
- Public-export preflight path is executable or explicitly marked as external.
- All internal links resolve.
- Release checklist includes public-surface, artifact-boundary, claim accuracy, generated-vs-source separation, and sync-from-private provenance checks.

### Verification Path

1. Run the documented public-export preflight or record why it is unavailable.
2. Check all internal links and file references.
3. Run `git diff --check`.
4. Manually scan for secrets, private references, generated logs, and unsupported claims.
