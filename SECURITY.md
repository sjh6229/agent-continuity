# Security Policy

Agent Continuity is designed to avoid collecting secrets and personal work history. It still writes project-local notes, so treat those notes as source files that deserve review before publishing.

## Supported Versions

Security fixes are handled on the default branch until versioned releases are added.

## Reporting a Vulnerability

Use GitHub private vulnerability reporting when available. If the repository does not have private reporting enabled, open a minimal public issue that describes the affected area without including secrets, tokens, private URLs, or customer data.

## Sensitive Data Rules

Do not include sensitive values in bug reports, examples, screenshots, logs, fixtures, or pull requests.

Sensitive values include credentials, environment values, private URLs, customer data, personal identifiers, raw chat transcripts, and local home paths.

## Maintainer Checklist

Before merging a release-facing change:

1. Run `python scripts/privacy-scan.py .`.
2. Review changed examples manually for synthetic data only.
3. Confirm generated images contain no readable paths, logs, keys, names, or screenshots.
4. Confirm the installable skill remains small and does not include private project documentation.
