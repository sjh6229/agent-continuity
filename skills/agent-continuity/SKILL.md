---
name: agent-continuity
description: Use when initializing, resuming, continuing, handing off, or closing a long-running AI coding project across sessions, especially for initialize continuity notes, set up handoff notes, create docs, resume work, continue later, handoff, next session, long-running project, session state, continuity notes, docs/START_HERE.md, docs/CURRENT_STATE.md, docs/PROGRESS.md, docs/DECISIONS.md, or the legacy keyword longwork.
---

# Agent Continuity

Use this skill to keep long-running project work resumable through short, privacy-first continuity notes.

## Initialize Workflow

Use this workflow when a user wants to start a long-running project, set up continuity notes, create handoff docs, or prepare work that will continue across sessions.

1. Identify the actual target project folder. Do not create continuity notes in a scratch directory unless the scratch directory is the user's actual project.
2. Read project instructions first, especially `AGENTS.md`, `CLAUDE.md`, or nested instruction files.
3. If the target folder or tracked work is unclear, ask one concise question before creating files: `What long-running work should these notes track, and what is the first success criterion?`
4. If `docs/` or continuity files already exist, do not overwrite them. Read existing notes, then create only the missing files that are needed.
5. Create or update `docs/START_HERE.md`, `docs/CURRENT_STATE.md`, `docs/PROGRESS.md`, and `docs/DECISIONS.md` using `references/state-notes.md`.
6. Keep initial notes neutral and minimal when details are not yet known. Do not invent project history, decisions, blockers, or verification results.
7. Verify the created files exist and contain only the minimum state needed to resume.
8. Report the created files and the first recommended next action.

## Start Workflow

1. Identify the actual target project folder. Do not assume the current scratch directory is the project if the user names another folder.
2. Read project instructions first, especially `AGENTS.md`, `CLAUDE.md`, or nested instruction files.
3. If `docs/START_HERE.md` exists, read it before project notes.
4. If `docs/CURRENT_STATE.md` exists, read it before proposing or resuming work.
5. Read only the needed parts of `docs/PROGRESS.md`; prefer recent entries or targeted search.
6. Read `docs/DECISIONS.md` when implementation direction, stack, data model, or operational policy matters.
7. State success criteria and verification method before editing when project instructions require it.
8. If code or document edits need approval, show a short plan and wait.

## During Work

- Keep every changed line tied to the user's request, success criteria, or verification.
- Treat continuity notes as project-local state, not public output, personal memory, or chat history.
- Never store credentials, environment values, API keys, tokens, passwords, private keys, private URLs, customer data, personal identifiers, absolute local home paths, raw chat transcripts, or raw logs that may contain secrets.
- If sensitive context matters, write a generic redaction such as `private service`, `local config file`, or `redacted credential`.
- If the user asks for a narrow one-off task, do not update continuity notes unless the task clearly changes the long-running project state.
- If unrelated problems appear, report them instead of folding them into the current scope.

## Closeout Workflow

Use `references/state-notes.md` when updating continuity files.

1. Decide whether continuity notes need an update.
   - Update when the task changed project state, left unresolved next actions, made a durable decision, or affects the next session.
   - Skip when the task was read-only, exploratory, unrelated, or too narrow to change project state.
2. Update `docs/CURRENT_STATE.md` as a short current snapshot only.
3. Append one dated entry to `docs/PROGRESS.md`; do not rewrite old log entries.
4. Add to `docs/DECISIONS.md` only for durable design, stack, data, workflow, or operational decisions.
5. Verify changed note files contain only the minimum state needed to resume.
6. In the final report, include changed files, verification run, remaining blockers, and next action when useful.

## Output Rules

- Keep final answers concise and in the user's language.
- Do not put prompt, agent, instruction, security-review, compliance, or process language into public deliverables.
- If Git work was involved and project instructions ask for it, report `git status`, changed files, and raw test output.
