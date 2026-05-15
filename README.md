# Agentic Systems Verifier Case Study

A public case study for an agentic verification workflow that connects systems engineering, model-based architecture review, and retrieval-augmented evaluation.

This repository intentionally contains no production source code, datasets, copied standards material, grant material, cloud deployment files, credentials, or build logs. It is a sanitized portfolio artifact that explains the engineering approach at a public boundary.

[Watch the demo](https://youtu.be/zYuLUAMb0So)

## What This Shows

- Agentic review of systems-engineering artifacts
- RAG-grounded evidence selection for technical review
- Traceability and faithfulness checks across architecture inputs
- A public-safe architecture pattern rather than a source dump

## Problem

Complex cyber-physical systems produce requirements, architecture models, design assumptions, and verification evidence across multiple tools. Reviewing those artifacts manually is slow, error-prone, and difficult to scale.

The project explored how an agentic verification workflow can help:

- parse structured architecture inputs
- retrieve relevant requirement context
- evaluate answer faithfulness against source material
- surface traceability gaps
- support human review instead of replacing it

## Architecture Pattern

The demonstrated pattern used modular layers:

1. Ingestion layer for source documents and structured model artifacts.
2. Parsing layer for model-oriented text and requirement-like records.
3. Retrieval layer for contextual evidence selection.
4. Verification layer for faithfulness, precision, and recall-style scoring.
5. Review UI for inspecting generated conclusions and evidence.

The public takeaway is the pattern, not a full implementation dump.

## What Was Demonstrated

- Agentic decomposition of a systems-engineering review task.
- Retrieval-augmented evidence grounding.
- LLM-as-reviewer scoring for faithfulness-style checks.
- A web-facing mission-control style interface.
- Batch-style processing of technical source material.

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
