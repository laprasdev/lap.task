---
name: lap-task
description: Create or resume a Workbench task using the project's rules, researched scope, target architecture, dependencies and acceptance checks. Invoke explicitly to establish tracked work and guide its implementation and review.
license: MIT
metadata:
  display-name: lap.task
---

# lap.task

Establish the requested work in the Workbench pattern. The result is an actionable desk task, or a small set of related tasks, with the considerations needed to build and review it. Follow the user's requested extent: creating or planning a task does not by itself request implementation; a request to implement continues through the authorized work after setup.

Workbench owns task state, claims, dependencies, questions, review evidence and handoff context. Use the existing desk and project rules rather than creating another task system. This skill grants no additional tool permissions or publishing authority.

## Find the project and its rules

Read the shared policy, `/Users/lap/Development/agent-rules/AGENTS.md`, plus the applicable repository and nested `AGENTS.md`/`CLAUDE.md` files. Follow their references relevant to the files and consumers involved. Record the source paths and the requirements that affect this task in its spec. Keep rules in their owning files; do not copy an entire rule system into each task or silently relax it. Language limits, engine mechanisms, review roles and release procedures apply in their declared scope. If applicable rules conflict materially, identify their sources and resolve the conflict with the owner before dependent work.

Use `wb`, or the Workbench checkout's `bin/wb.mjs` through Node when `wb` is not on PATH. On the owner's Mac the fallback is `node /Users/lap/Development/workbench/bin/wb.mjs`. Reuse an existing `WB_AGENT`, otherwise set it once to identify the client and task. Respect an existing `WORKBENCH_URL`.

Run `wb projects`, then `wb next <project>`. Match the request and repository to the registered project; one repository can serve several desk projects. Read existing task specs, notes, owner answers, claims and the checkpoint path before adding anything. The agent endpoint `GET /api/agent/next/<project>` supplies readiness and task descriptions, but not agent-written note history. For a task's full record, read `GET /api/projects` on the configured desk and follow each same-origin `next` URL until it is null. Use the same authenticated connection for every page; never print its credential. The Workbench checkout's `projectCollection.ts` exports `collectProjects` for this contract. From the combined `projects`, select the matching project and exact item ID in `items.todo`, `items.feedback`, `items.ask` or `items.checkpoints`, and read the relevant `status.log` entries plus `reply`. Use these records for reviewer findings, handoff evidence and owner context before resuming; do not assume the readiness brief contains them. Ask only if the project or task remains ambiguous. If the project is unregistered or the desk is unavailable, report the specific connection or registration gap and continue independent research; do not claim integration succeeded or silently create a file-based replacement.

For existing work, reuse its task ID and history. Do not duplicate tasks, take another session's claim, reopen accepted work, or infer owner approval from a status or silence. Read any project-required task documents too; see [Existing task documents](existing-documents.md).

## Research the work

Audit enforcement as well as prose. Find the active language/migration policy, compiler inclusion and strictness, local check commands, CI invocations and page/component ownership checks. For each applicable mechanical rule, record its canonical source, enforcing command and an observed rejection case; identify missing gates as work rather than describing them as enforced. Follow references to prior owner-approved migration decisions even when the entry document is stale. Verify the current client actually loads the shared policy.

Before implementation, run the shared policy's search and consumer audit over related symbols, patterns, callers, data flow and tests, and record the owners and consumers you found in the spec. Hold the proposed change to the policy and the repository's rules. Present alternatives only when a real tradeoff needs the owner's decision; two mechanisms for one job are a defect to collapse, not alternatives, and do not manufacture a fixed number of approaches.

## Establish the architecture maps

Read `wb architecture <project> --snapshot current` and verify the existing code before implementation: relevant components, classes/methods and functions, locations, dependencies and states. Save with `wb architecture <project> <file.json> --snapshot current`, retaining Current's own revision. Current accepts only verified `present` symbols or real `stubbed` skeletons. Its first save fixes Start once with its author/date. Start is the first recorded baseline, not invented project-begin history; it cannot be edited. Do not copy planned Target symbols into Current or claim a historical baseline when none was captured.

Read `wb architecture <project>` for Target. Before implementation, declare or reconcile the intended components, relevant classes/methods and functions, source locations and component dependencies. Use the Workbench checkout's `architecture.example.json` for the current format.

- `planned`: intended, not yet implemented.
- `stubbed`: an actual code skeleton exists.
- `present`: the named implementation has been checked in the code.

Map first; create code skeletons only when the task needs them. Keep class/function names expressive and responsibilities abstract. The Architecture section compares Start → Current → Target, with independently hideable columns; hiding Current does not change the Target comparison base. Keep the map high-level and connect the task spec to the components it builds. Preserve unrelated components and their stable IDs. Read the current map to a temporary JSON file, retain its `revision`, and save with `wb architecture <project> <file.json>`. On a stale-write refusal, reread and reconcile; never overwrite a newer map. A declaration is neither implementation evidence nor owner approval.

## Create the desk task

Use [Workbench templates](workbench-templates.md) when a task needs a reusable specification, cross-project handoff, run/evidence record or review submission. Adapt the depth to the task; the examples do not add permissions, reviewer substitutions or universal execution requirements.

Follow the project's planning/reviewer arrangement. Where the shared rules assign checkpoint planning to Fable's reviewer, obtain that gameplan and have the reviewer record the task specs. Respect the configured fallback if the reviewer is unavailable, and report any remaining review blocker honestly. Do not invent a reviewer verdict or spend credits to bypass a limit. If required planning review cannot run, record the researched scope on the desk as awaiting that review and keep dependent implementation pending.

Each task needs a 1–3 word title and a spec containing the following, at a depth proportionate to the change:

- **Outcome and scope:** observable behavior, acceptance cases, and behavior to preserve.
- **Rules:** applicable source paths, the requirements relevant here, and any owner-approved exceptions.
- **Approach and ownership:** verified symbols, files, architecture components, reusable mechanisms, and affected consumers with expected changes.
- **Dependencies:** what must finish first and which existing checkpoint the task feeds, when one fits.
- **Checks:** the tests, build, consumer checks and visual/interaction evidence that prove the outcome; include the enforcing command and rejection case for each new mechanical guard, and distinguish compiler coverage from legacy compatibility. Note anything not yet verifiable.
- **Decisions:** approval already given, unresolved owner choices, and any material scope or structural decision still required.

Desk text is Markdown. It reaches `wb` with real newlines through a heredoc, and a picture shows inline as `![caption](/media/<project>/<sha256 of its bytes>.<ext>)`, the same file attached to its card with `wb attach … --image`.

Use `wb add <project> "<title>" "<spec>"`, with `--for` and `--after` as the policy's Desk rule 2 says. Split work when pieces have distinct outcomes or dependencies; do not inflate a small request into a new project or checkpoint. When no existing checkpoint fits, ask the owner on the desk instead of manufacturing a milestone.

Amend an unfinished task with `wb amend <project> <id> "<title>" "<spec>"` only within the current agent's authority, preserving its history and approved scope. Do not rewrite a baseline to conceal a changed outcome. Add research, evidence and handoff context with `wb note <project> <id> "<text>"`.

Put unresolved owner decisions on the desk with `wb ask <project> "<question>" "<context>"`, and reference the ask from the task. Make the result concrete before seeking required approval.

Finish setup by reporting the project and task IDs, checkpoint/dependency links, architecture status, and the next ready step or pending decision. A planning-only request ends here with the work established on the desk.

## Build, review and resume

When implementation is requested and authorized, take ready work first and run `wb claim <project> <id>` before starting. If refused, respect the existing owner; continue another authorized ready task or report the conflict. Keep task notes current at meaningful milestones, including discoveries, blockers, decisions and checks with actual results. Re-read current state when resuming; the desk holds what the next session needs.

At closeout, before review and `wb done`, refresh Current against the actual code and reconcile Target: verify symbols, locations, dependencies and states, keeping unfinished target pieces `planned`. Retain each snapshot's own revision and leave Start untouched. Run the relevant acceptance checks and record evidence and limits. For visible changes, inspect the real layouts and interactions required by the project's design rules.

Run the policy's review loop (Desk and review); only after its approval, submit `wb done <project> <id> "<summary, checks, review rounds and verdict>"`. If review cannot run, leave an accurate note and report the pending review rather than marking it passed.

For an accepted/completed task, obtain direction before reopening or widening its scope. For an awaiting-review task, preserve its state and work only on authorized revisions.
