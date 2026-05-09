# Verification Plan

## Checks

Run the public-export gate before publishing changes:

```bash
python3 repo_preflight.py --repo . --profile public-export --paranoid
```

Manual review:

- Confirm no credentials, API keys, datasets, copied standards, private planning notes, or build logs are present.
- Confirm public claims remain case-study claims, not production, compliance, or safety claims.
- Confirm links point only to public demos or public repositories.

## Release Decision

Release only when automated checks and manual boundary review pass.

