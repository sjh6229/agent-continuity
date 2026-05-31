# Privacy Model

Agent Continuity keeps long-running work resumable without creating a broad personal memory store.

## Principle

Write the minimum project state needed for the next useful session.

Continuity notes should explain where the project is, what changed, what remains blocked, and which durable decisions matter. They should not record the full history of a person, chat, machine, client, or workspace.

## Allowed Content

- project goal
- current implementation status
- changed files or changed areas
- verification already run
- known blockers
- next actions
- durable decisions, reasons, and impact

## Disallowed Content

- credentials, API keys, access tokens, passwords, private keys, and secret values
- environment variable values
- private URLs, internal dashboards, private repository links, or private support links
- customer records, client names, personal identifiers, or production data
- absolute local home paths
- raw chat transcripts
- raw terminal logs that may contain secrets
- unreleased business metrics, pricing, roadmap, or strategy details
- personal productivity notes unrelated to project state

## Redaction Rules

Use generic labels when context is necessary:

- `private service` instead of an internal URL
- `local config file` instead of a full home path
- `redacted credential` instead of a secret value
- `customer record` instead of a real identifier

Do not paste the original value next to the redaction.

## Update Rules

Update continuity notes only when the project state changed, a next session would otherwise lose important context, or a durable decision was made.

Skip updates for read-only research, quick answers, narrow one-off tasks, or work unrelated to the long-running project.

## Public Release Review

Before publishing a repository that contains continuity notes:

1. Run the privacy scanner.
2. Search for project-specific names with `--term`.
3. Open every example note and confirm it uses synthetic data.
4. Inspect generated images for readable text, paths, names, keys, or screenshots.
