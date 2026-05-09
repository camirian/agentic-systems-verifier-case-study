# Case Study: Agentic Verification for Systems Engineering

## Context

Systems engineering review often requires checking whether claims about a system are supported by requirements, architecture models, interface definitions, and verification evidence. The workload is document-heavy and benefits from repeatable evidence retrieval.

The project explored an agentic review workflow for this problem. The public lesson is that a useful verifier should be designed as a decision-support system, not as an autonomous authority.

## Workflow

1. Normalize source artifacts into reviewable chunks.
2. Extract structured signals from architecture and requirement-like inputs.
3. Retrieve relevant evidence for each claim.
4. Ask a model to produce a bounded assessment against retrieved context.
5. Score output for faithfulness, precision, and recall-style behavior.
6. Present results to a human reviewer with links back to evidence.

## Design Principles

- Keep source evidence visible.
- Separate parsing, retrieval, scoring, and presentation.
- Treat model outputs as review candidates.
- Prefer measurable scoring over broad qualitative claims.
- Keep deployment and model-provider assumptions replaceable.

## Engineering Lessons

- Retrieval quality controls verifier quality.
- Traceability UX matters as much as model output.
- Evaluation harnesses should be built early.
- Batch workflows are useful for repeatable regression checks.
- Sensitive technical corpora require strict release boundaries.

## Public Outcome

The public artifact is this case study plus the demo video. The released material focuses on the reusable engineering pattern and omits implementation details that require separate review.
