---
name: lap-task
description: Create, resume, and track a coding task through research, owner signoff, implementation, and review, with an approved definition and an append-only progress journal.
license: MIT
metadata:
  display-name: lap.task
---

# lap.task

Use this workflow when the user explicitly requests a tracked task. The user's request, project instructions, and host permissions determine its scope. Invoking the skill does not authorize unrelated work or grant additional permissions.

## Locate the task

Read the applicable `AGENTS.md`, `CLAUDE.md`, and relevant guides they reference. Reuse the project's task location and naming convention. Look for existing `definition.md` and `progress.md` pairs within the project before creating anything.

If the project has no task convention, use `docs/tasks/{task-name}.MM_DD_YY/`, with the current local date. Keep the task name to one directory component. If multiple existing tasks match, ask which one to resume. If a matching directory is missing one of its documents, report the incomplete task instead of overwriting or silently recreating it.

For a new task, follow Research through Review below. For an existing task, follow Resume.

## Research

Research before changing implementation code.

1. Search related concepts, symbols, callers, and tests. Start from the assumption that useful patterns already exist.
2. Trace the relevant data flow and call sites. Identify reusable abstractions and their consumers.
3. For shared changes, list the behavior change for every affected consumer. Narrow the proposal where impact is unverified.
4. Identify duplicate or unused code, but verify its consumers and ownership before proposing removal. Preserve intentionally retained capability.
5. Answer: can composition of existing pieces solve this; can configuration or validation express the behavior; does an existing pattern already cover the need?

## Proposal and signoff

Present the outcome, alternatives with tradeoffs, affected files, anticipated additions/deletions, verification, and any unresolved questions. Aim for three meaningful approaches; explain when fewer are credible instead of inventing filler.

Prefer extending existing mechanisms and reducing duplication. Estimate the net code change and justify growth when it is necessary.

Wait for the owner's explicit approval of the proposed scope before implementation. If the owner has already approved that same concrete scope in the conversation, record that approval and continue without asking again. A skill invocation alone does not approve an as-yet-unspecified plan.

## Create the documents

After signoff, create both documents using the supplied templates:

- [definition-template.md](definition-template.md) becomes `definition.md`, the approved baseline.
- [progress-template.md](progress-template.md) becomes `progress.md`, the working journal. Set its status to `IN PROGRESS`.

Fill in the actual goal, acceptance cases, research, approach, affected files, and task-specific deliverables. Record the scope the owner approved. Never invent an approval or mark research checks that were not performed.

Treat `definition.md` as fixed unless the owner explicitly approves a particular amendment. Record the reason and approval in `progress.md` before making an approved amendment. Ordinary discoveries, blockers, and pivots belong in `progress.md`. This is a workflow rule, not a filesystem lock.

## Execute

- Work within the approved scope and the host's current tool permissions. Follow the repository's architecture, naming, logging, and size limits; do not import another project's limits.
- Search before creating a parallel mechanism. Keep each piece responsible for one concern and preserve unrelated changes.
- Append dated accomplishments, blockers, resolutions, and pivots at meaningful milestones. Preserve previous journal entries and checklist items; update status and checkboxes as facts change.
- For a material change to the approved approach or scope, explain the impact and obtain approval. Do not quietly rewrite the baseline to match the implementation.
- Run checks appropriate to the change. Record commands, real results, and limits. Do not hide invalid state with silent fallbacks or weaken checks to make them pass.
- If access, authentication, or sandbox restrictions prevent an action, report the exact blocker. Approval of a plan does not override those restrictions.

## Review

Work through the task-specific deliverables and progress checklist. Mark only the items supported by evidence. Report what changed, checks and results, net code change, and outstanding concerns.

Set status to `AWAITING REVIEW`. Only the owner confirms completion. After explicit confirmation, record that confirmation and set `COMPLETE`; never infer acceptance from silence or passing tests.

## Resume

Read the existing definition and progress before changing anything. Report the last status, approved scope, accomplishments, and unresolved blockers. Continue with the user's requested next step when it is clear and authorized; ask where to resume only when it is unclear.

If status is `AWAITING SIGNOFF` or `AWAITING REVIEW`, preserve that gate unless the owner has supplied the corresponding approval. For a completed task, obtain direction before reopening it or changing its scope.
