# Case Study: Agentic Verification for Systems Engineering

> **Evidence boundary:** This is an unverified historical narrative. The public
> repository contains no implementation, dataset, run logs, scores, or demo
> that can reproduce or independently verify the described workflow or lessons.


## Context

Systems engineering review can require checking whether claims about a system
are supported by requirements, architecture models, interface definitions, and
verification evidence. This is problem framing for the historical account, not
an empirical finding from this repository.

The historical account describes exploring an agentic review workflow. Its
design recommendation is to treat a verifier as decision support rather than
autonomous authority; this repo does not contain evidence that the approach was
implemented or evaluated.

## Described Workflow (Not Reproducible Here)

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

## Reported Design Considerations (Unverified)

- Retrieval quality controls verifier quality.
- Traceability UX matters as much as model output.
- Evaluation harnesses should be built early.
- Batch workflows are useful for repeatable regression checks.
- Sensitive technical corpora require strict release boundaries.

## Public Outcome

The public artifact is this case study. It presents a conceptual engineering
pattern and omits implementation details that require separate review; the
public repository does not establish that the pattern was implemented or
validated.
