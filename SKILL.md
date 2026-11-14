---
name: lap.task
description: Create or resume a Workbench task with the applicable rules, research, target architecture, dependencies and acceptance checks. Invoke explicitly to establish tracked work.
argument-hint: "<task request or existing task ID>"
disable-model-invocation: true
user-invocable: true
---

# lap.task

Read [the task workflow](skills/lap-task/SKILL.md) and follow it for the user's request. Resolve its supporting links relative to that workflow's directory.

Task request: $ARGUMENTS

Use the current project's instructions and the session's existing permissions. This command grants no additional tools, file access, network access, or authority to publish.
