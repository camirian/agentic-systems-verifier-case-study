# Verification Plan

## Checks

Run the self-contained public-export gate before publishing changes:

```bash
python3 scripts/verify_public.py
```

This stdlib-only script resolves internal markdown links and scans tracked text
files for forbidden patterns (`.env` contents, credentials, API keys). It exits
non-zero on any failure. Treat a non-zero exit as a release blocker.

Manual review:

- Confirm no credentials, API keys, datasets, copied standards, private planning notes, or build logs are present.
- Confirm public claims remain case-study claims, not production, compliance, or safety claims.
- Confirm links point only to public demos or public repositories.

## Release Decision

Release only when automated checks and manual boundary review pass.

