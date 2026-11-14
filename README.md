# lap.task

Create or resume a Workbench task using the project's rules, researched scope, target architecture, dependencies and acceptance checks. The command establishes the work on the desk, then guides implementation and review when requested.

The rules stay in their shared, repository and nested instruction files. Each task records which requirements apply and how its result will be verified. Workbench owns status, claims, questions, dependencies, review evidence and handoffs. Existing project-required definition/progress documents remain supported; new tasks do not create them by default.

## Use

In Claude Code:

```text
/lap.task establish the graph shaping work
/lap.task resume todo:example
```

In Codex:

```text
$lap-task establish the graph shaping work
$lap-task implement the ready task we just planned
```

Setup resolves the registered desk project, reuses existing work where appropriate, reads the applicable rules and consumers, reconciles the target architecture, and records a task spec with real dependencies and acceptance checks. The result includes the project/task IDs and the next ready step or pending owner decision. Planning alone does not start implementation. Existing approval carries forward; required owner decisions and reviewer approvals are never fabricated.

The current project needs access to its Workbench desk and CLI. The workflow uses `wb`, with a Node fallback to the Workbench checkout's `bin/wb.mjs`. The CLI honors `WORKBENCH_URL`; retain the configured desk endpoint. If the desk or project is unavailable, the agent reports that gap and may continue independent research, but does not silently create a competing task system.

## Install across projects

Clone into your personal Claude skills directory:

```sh
git clone https://github.com/laprasdev/lap.task.git ~/.claude/skills/lap.task
```

If you set `CLAUDE_CONFIG_DIR`, use its `skills/lap.task` directory instead. Inspect an existing installation rather than overwriting it. Start a fresh Claude session if `/lap.task` is not listed.

The reusable workflow is `skills/lap-task`; the root `SKILL.md` is only the Claude command adapter. To make the same maintained source available to Codex across projects, link it into the personal skills directory:

```sh
mkdir -p ~/.agents/skills
ln -s ~/.claude/skills/lap.task/skills/lap-task ~/.agents/skills/lap-task
```

Use the actual clone location if different. The command refuses an existing destination; inspect that destination rather than replacing it. Codex supports symlinked skill directories. The skill remains explicit-only and is invoked as `$lap-task`. Codex detects skill changes automatically; restart it if discovery has not refreshed. See the [official OpenAI skills documentation](https://learn.chatgpt.com/docs/build-skills).

Update the clone deliberately with `git -C ~/.claude/skills/lap.task pull --ff-only`, resolving local edits first. The symlink keeps both clients on the same workflow. Installation on another machine requires the updated package, that machine's project rules and Workbench access; it does not copy conversations, credentials or owner approvals.

## Existing task documents

Projects such as Bloom may still require an approved `definition.md` and a historical `progress.md`. The workflow's [existing-document guidance](skills/lap-task/existing-documents.md) preserves that requirement and links the documents to the desk task. Workbench remains the source of current state and handoff context.

The optional `hooks/definition-reminder.py` supplies context before Claude's Edit/Write tools change an existing task definition beside a progress file. It is retained for those projects, is not enabled by installation, and neither verifies approval nor locks files. To enable it deliberately, merge the following entry into `hooks.PreToolUse` in your Claude settings, preserving existing entries and using the actual clone path:

```json
{
  "matcher": "Edit|Write",
  "hooks": [
    {
      "type": "command",
      "command": "python3 \"/absolute/path/to/lap.task/hooks/definition-reminder.py\""
    }
  ]
}
```

## Permissions and origin

The skill grants no file, network, publishing or approval authority. The owner controls scope and acceptance; the project configures planning/review roles; the host controls tool permissions. It never answers owner calls or edits `answers.json`. Cloning does not change sandbox settings or enable hooks.

Adapted from BloomGameClient's `.claude/skills/task` workflow under the MIT license, now using the owner's Workbench task pattern. The original Bloom `/task` remains separate. Claude Code's built-in `/tasks` manages background activity and is unrelated.
