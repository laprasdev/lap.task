---
name: lap.task
description: Create or resume a task with research, owner signoff, an approved definition, and a progress journal. Invoke explicitly for work you want tracked through review.
argument-hint: "<task-name or task-directory>"
disable-model-invocation: true
user-invocable: true
---

# lap.task

Read [the task workflow](skills/lap-task/SKILL.md) and follow it for the user's request. Resolve that workflow's template links relative to its own directory.

Task request: $ARGUMENTS

Use the current project's instructions and the session's existing permissions. This command grants no additional tools, file access, network access, or authority to publish.
