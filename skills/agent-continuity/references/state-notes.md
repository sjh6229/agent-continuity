# Agent Continuity State Notes

Use these templates when creating or updating project-local continuity notes.

## CURRENT_STATE.md

Keep this file short. It should describe the current state, not the full history.

```markdown
# Current State

## Goal
- ...

## Current Status
- ...

## Changing Files
- ...

## Known Issues
- ...

## Next Actions
- ...
```

## PROGRESS.md

Append one dated entry per meaningful work chunk.

```markdown
## YYYY-MM-DD HH:mm
- Changed: ...
- Verified: ...
- Remaining: ...
```

## DECISIONS.md

Record only durable choices.

```markdown
## YYYY-MM-DD - Decision title
- Decision: ...
- Reason: ...
- Impact: ...
```

## Privacy Guardrails

Do not write credentials, environment values, API keys, tokens, passwords, private keys, private URLs, customer data, personal identifiers, absolute local home paths, raw chat transcripts, or raw logs into continuity notes.

Use generic redactions such as `private service`, `local config file`, `customer record`, or `redacted credential` when context is needed.
