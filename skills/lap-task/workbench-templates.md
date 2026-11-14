# Workbench task and review templates

Use these shapes when establishing or reconciling tracked work. Keep small tasks small: omit sections that add no useful information. The desk holds current scope and readiness; notes preserve discoveries and superseded evidence. These templates do not change the project's rules, reviewer policy, claims or owner approvals.

## Task specification

````markdown
{One short lead paragraph: the observable outcome, its delivery context and acceptance boundary.}

## Change

- {The approach: verified existing mechanisms, affected consumers and behavior to preserve.}
- {What can proceed now: independent research, fixtures, authoring or implementation.}

## Files

- {The implementing owner and canonical repository/checkout; the files and consumers it touches, relative paths in code spans and absolute paths bare.}

## Rules

- {Only where the task has them: relevant rule-source links and applicable owner decisions.}

## Decisions

- {Only where the task has them: unresolved choices; readiness (local prerequisites, external project/task references and required capability); the next gate (the artifact, decision or result needed, and who supplies it).}

## Checks

- {Concrete input/action → observable output; the relevant reset/exit case.}
- {A consumer compatibility or regression case that matters.}
- {The required check or demonstration, current artifact/run reference, and review scope.}

```architecture
{the Target component ids the spec names}
```
````

Do not turn every task into a full project specification. A short correction may need one paragraph and one verification step. Separate tasks when outcomes have different owners, execution contexts or real dependencies. Before splitting, inspect existing integration tasks and checkpoint contracts; preserve every agreed deliverable and record its new home without duplicating it. Reuse existing IDs; an amendment preserves earlier scope in history. Read accepted/source-owned records before changing anything that depends on them.

## External dependency and handoff

Workbench dependency edges are project-local. Name an external dependency in the consumer spec without inventing a local edge or declaring it satisfied from another project's task title.

```markdown
Producer: {project/task ID, owner and canonical source}
Consumer: {project/task ID and integration owner}
Required capability: {minimum supported behavior, modules/assets and outputs}
Compatibility: {authored fields/IDs and semantics to preserve; ABI/protocol status}
Candidate for validation: {exact local build/commit/digest, schema and capability evidence; or pending}
Consumer validation: {who runs which cases against that candidate; task receiving results/failures}
Release/pin gate: {producer release identity and checks needed for a maintained consumer pin}
Independent work: {what can progress before the capability exists}
Current gate: {ready/pending/unverified, dated evidence and next owner action}
```

A candidate may be tested before a release is finalized. Do not make the producer's release depend on consumer validation while also requiring that release before the consumer can validate. A contract, fixture or renderer can support preparation without proving execution. Keep compatible authored data distinct from a still-draft host ABI. Unsupported capabilities remain explicit; do not reauthor application behavior to conceal them.

When a candidate changes, identify which consumer evidence needs refreshing; previous results keep their original build identity.

A first usable capability slice need not wait for full module parity. Conversely, a first locomotion slice does not imply support for timers, contacts, material composition or every consumer. Avoid placing optional integration beneath a root checkpoint that gates otherwise independent delivery.

## Run and evidence record

Attach the useful artifact inline to its task. Keep a separate run record for each build and execution context. Reference it from dependent tasks instead of copying an undated “latest result” paragraph into each one.

Verify evidence in its actual delivery surface: play any uploaded clips and load any embedded previews from the task itself. A standalone page pass does not prove that its Workbench frame works. If embedding is unsupported, retain inline recordings/images, provide a working launch link and record the embedding gap with its owner; do not present a blank frame as usable evidence.

```markdown
Artifact: {commit, or dirty worktree + base HEAD + scoped file digest; digest scope}
Source: {repository/checkout, authored configuration/asset IDs and selected consumer/profile}
Runtime: {candidate/build/version + exercised capabilities, or “no engine — authoring/diagnostic sample”}
Run: {date/time, environment, character/model and relevant input/clock settings}
Delivery: {live browser execution / recorded native execution / authoring inspection / diagnostic playback}
Launch: {working URL or local command; exact state/scenario selection and reset instructions}

| Case | Action/input | Expected | Observed | Result | Evidence |
| --- | --- | --- | --- | --- | --- |
| {case} | {repeatable setup/action} | {observable result} | {measured result, or not run} | {pass/fail/pending/blocked} | {image/video/trace link} |

Limits/next: {what this run cannot establish; next concrete action and owner}
```

Match proof to the claim. Show a character performing a mechanic when that is the requested outcome. A control panel proves authoring behavior; a clip player proves rendering/playback. Neither establishes that the engine evaluated the mechanic. A native recording can prove native behavior while browser execution remains pending. Separate these gates when the agreed deliverables allow independent progress.

Use video or time-indexed traces for timing/oscillation claims; a still cannot establish frequency. A timeout, stale log or previous green result does not verify a later artifact. Mark evidence that predates a change. Distinguish a reachable frame from correct state selection, usable input, engine connection and the claimed result. Record temporary preview service dependencies; static captured evidence should remain accessible separately.

## Review and submission

```markdown
Artifact reviewed: {same identity/scope as the change and evidence}
Reviewer: {actual reviewer and applicable assignment or owner-authorized substitution}
Rounds/findings: {findings, fixes or evidence-based dispositions}
Verdict: {approved/revise/pending, and precisely what was reviewed}
Checks: {automated results; observed behavior; unrun or blocked cases}
Owner acceptance: {pending, or reference the owner's actual response}
Next: {submit for review, fix a finding, validate a candidate or await the named decision}
```

Keep static review, automated checks, live/recorded behavior and owner acceptance separate. A review of task wording does not approve its future implementation. `wb done` submits a finished, reviewed task to the owner; it does not answer the owner or sign their seat. A reviewer substitution is limited to the owner's stated scope and never rewrites the global policy. Use the project's required review loop.

## Checkpoint outline

Use this when the owner authorizes checkpoint planning or refinement; it is not permission to change a destination.

```markdown
Outcome: {what can be demonstrated at this checkpoint}
Feeds: {owner's existing destination or next checkpoint}
Needs: {only the prerequisites that genuinely gate this outcome}
Tasks/owners: {small owned outcomes; link the existing task IDs}
Proof: {which artifact and behavior establish the outcome in the required context}
Review: {project-required reviewer gate and separate owner acceptance}
```

Check both task and checkpoint dependencies. A task can be blocked by the prerequisites of its checkpoint even without an explicit task edge. Preserve accepted work and existing owner decisions; never reset statuses to make a revised plan look tidy.

## Worked patterns from the current projects

**Power Ups mechanic evidence:** Outcome is Blue and Chroma actually performing dip → intro → sustained power → warning → expiry, plus refill and rival replacement. Existing OSC assets own the behavior. Native video/traces can establish the original Unity demo. A separate browser-integration task identifies the needed C++ candidate capabilities. Refill preserves the current power, replacement applies the rival after its intro, and final exit restores baseline. Material swatches are supplementary evidence.

**Shared runtime handoff:** Core owns the authored-data contract, evaluator and versioned output capabilities; design-suite owns presentation; Synth owns editing and connection; application owners supply their authored cases. Validate a candidate on representative consumers, then record a pinned release. Full parity remains a later, explicit gate.

**Control or asset preview:** Identify the actual control kind/form or model/clip and its source. Capture the real layout/interaction or rig/playback result. State whether it edits an authored asset, runs temporary sample values, or receives engine output. Keep this task's acceptance distinct from the later gameplay demo.
