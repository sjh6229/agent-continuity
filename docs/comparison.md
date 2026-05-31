# Comparison

Agent Continuity is intentionally narrower than broad memory systems or autonomous runners.

| Approach | Best for | Tradeoff |
| --- | --- | --- |
| Agent Continuity | Safe session handoff for coding projects | Requires disciplined short notes |
| Single handoff file | Very small projects | Can become stale or too dense |
| Broad memory sync | Personal preferences and cross-project recall | Higher privacy and cleanup burden |
| Autonomous runner logs | Long unattended execution | Logs can collect noisy or sensitive data |
| Full project docs | Product and architecture documentation | Too heavy for session-to-session state |

## Design Choices

- Use "continuity notes" instead of "memory" to keep the scope narrow.
- Keep the installable skill small and move public documentation outside the skill folder.
- Prefer short Markdown files over hidden databases or raw transcripts.
- Store decisions separately from progress so old logs do not become the source of truth.
- Make note updates conditional so one-off tasks do not create unnecessary history.

## When Not To Use

Do not use Agent Continuity as a customer data store, credential notebook, chat archive, personal journal, or production incident log.
