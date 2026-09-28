# Agentic Systems Verifier Case Study

A documentation-only public case study presenting a historical, unverified
account of a conceptual agentic verification pattern for systems engineering,
model-based architecture review, and retrieval-augmented evaluation. No
implementation or experiment artifacts are published here to verify that
workflow.

This repository intentionally contains no production source code, datasets, copied standards material, grant material, cloud deployment files, credentials, or build logs. It is a sanitized portfolio artifact that explains the engineering approach at a public boundary.

## What This Case Study Describes

The following are topics in the historical account, not independently verified
capabilities of code available in this repository.

- An agentic review workflow for systems-engineering artifacts
- Evidence selection described as retrieval augmented generation
- Traceability and faithfulness checks across architecture inputs
- A public-safe architecture pattern rather than a source dump

## Problem Framing (Not Evaluated Here)

The historical account is motivated by a general proposition: cyber-physical
engineering reviews can involve requirements, architecture models, design
assumptions, and verification evidence across multiple tools. This repository
does not measure the review effort, error rate, or scalability of that process.

The historical account describes a proposed workflow that could:

- parse structured architecture inputs
- retrieve relevant requirement context
- evaluate answer faithfulness against source material
- surface traceability gaps
- support human review instead of replacing it

## Architecture Pattern

The historical account describes these conceptual layers:

1. Ingestion layer for source documents and structured model artifacts.
2. Parsing layer for model-oriented text and requirement-like records.
3. Retrieval layer for contextual evidence selection.
4. Verification layer for faithfulness, precision, and recall-style scoring.
5. Review UI for inspecting generated conclusions and evidence.

The public takeaway is the pattern, not a full implementation dump.

## Historical Behavior Descriptions

The earlier demo is no longer available. The behavior below is a historical
narrative account; this repository contains no implementation, dataset, run
logs, scores, or demo with which to reproduce or independently verify it.
These are not benchmarked results.

- Agentic decomposition of a systems-engineering review task.
- Retrieval-augmented evidence grounding.
- LLM-as-reviewer scoring for faithfulness-style checks.
- A web-facing mission-control style interface.
- Batch-style processing of technical source material.

For what is intentionally left out, see [What Is Not Included](#what-is-not-included)
and [docs/RELEASE_BOUNDARY.md](docs/RELEASE_BOUNDARY.md).

## Primary User

The intended reader is a technical reviewer, systems engineer, or portfolio
reviewer assessing the described workflow and public release boundary. This
repository reports no external user validation or measured success signal.

## Repo Verification Path

This repo is documentation-only (plus one stdlib verification script). The quickstart for local review is to read `README.md`, `docs/CASE_STUDY.md`, and `docs/RELEASE_BOUNDARY.md`, then run the self-contained pre-release gate before publishing changes:

```bash
python3 scripts/verify_public.py
```

It resolves internal markdown links and scans recognized text files for a
limited set of credential patterns. It does not inspect `.env` file contents;
the manual release review remains required. See `VERIFICATION_PLAN.md` for the
exact scope.

## What Is Not Included

- Original source code.
- Standards, vendor, government, or proprietary PDF material.
- Grant application content.
- Cloud deployment configuration.
- Planning notes, build logs, or operating instructions.
- API keys, model-provider configuration, or credentials.

## Public Artifacts

- [docs/CASE_STUDY.md](docs/CASE_STUDY.md)
- [docs/RELEASE_BOUNDARY.md](docs/RELEASE_BOUNDARY.md)

## Related Public Work

- Robotics glossary and SysML examples: https://github.com/camirian/robotics-ontology-public
- Sim-to-real control examples: https://github.com/camirian/sim-to-real-control-systems-public
- Articulated manipulation examples: https://github.com/camirian/articulated-robot-manipulation-public

## License

This case study is published for portfolio review. See [LICENSE](LICENSE).
