# Verification Plan

## Checks

Run the self-contained public-export gate before publishing changes:

```bash
python3 scripts/verify_public.py
```

This stdlib-only script resolves relative markdown links and scans recognized
text files found in the working tree (including untracked files) while
excluding the specific directories listed in the script. It checks a limited
set of credential patterns. It does not scan `.env` files or their contents,
binary files, external links, or every possible secret format. Treat a non-zero exit as a release blocker, and complete the manual
boundary review below for checks outside the script's scope.

Manual review:

- Confirm no credentials, API keys, datasets, copied standards, private planning notes, or build logs are present.
- Confirm public claims remain case-study claims, not production, compliance, or safety claims.
- Confirm external links point to intended public repositories. No demo is
  currently available.

## Release Decision

Release only when automated checks and manual boundary review pass.

