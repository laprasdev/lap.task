# Existing task documents

Some projects, including Bloom, explicitly require `definition.md` and `progress.md` alongside the desk. Keep that capability. Use these documents only when the applicable project instructions or owner require them; `/lap.task` does not create them by default.

Before resuming such a task, read both files and find its matching Workbench task. If no task exists, establish one using the recorded scope and evidence, with links or absolute paths to the documents. Preserve history and pending approvals. Do not treat an unchecked or disputed document claim as verified fact.

Use the project's task directory convention. If the owner requires new documents but the project has no convention, use `docs/tasks/{task-name}.MM_DD_YY/` with the current local date and a one-component name. Resolve ambiguous matches before writing. If a matching directory is incomplete, report that fact instead of overwriting it or fabricating the missing history.

The [definition template](definition-template.md) holds the approved specification. The [progress template](progress-template.md) holds detailed historical evidence. Record the desk project/task IDs in both. Workbench remains the source for live status, claims, dependencies, questions, reviewer findings and handoffs. Add a concise desk note when a document changes; do not make another session reconstruct current state from journal files.

Honor the project's definition-approval rule and existing authorization. Record approved amendments and their reason before changing the baseline. Append meaningful accomplishments, evidence, blockers and resolutions; do not erase earlier entries. Synchronize any document status from the actual desk state, distinguishing implementation finished, reviewer approved, and owner accepted. Only record completion after explicit owner acceptance.

The optional definition reminder hook remains available for these projects. It supplies context for Claude's Edit/Write tools, does not verify approval or lock files, and is not installed by this workflow.
