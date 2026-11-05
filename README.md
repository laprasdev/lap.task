# lap.task

A small, cloneable task workflow for Claude Code: research, owner signoff, implementation, and review. Each task has an approved `definition.md` and a `progress.md` journal that preserves its history.

`lap.task` is the first name in the `lap.*` family. This repository contains the skill, templates, and an optional local reminder hook. It needs no server, Workbench instance, subscription of its own, or API key. Claude Code uses the account already signed in on each machine.

## Install on another machine

Install Git and Claude Code, then clone this repository into your personal skills directory:

```sh
git clone https://github.com/laprasdev/lap.task.git ~/.claude/skills/lap.task
```

If you set `CLAUDE_CONFIG_DIR`, use its `skills/lap.task` directory instead. Git refuses to overwrite an existing destination; inspect or update an existing installation rather than deleting it.

Start a fresh Claude Code session in the project you want to work on, then enter:

```text
/lap.task improve-search
```

Claude researches the project and presents a proposal. After you approve the scope, it creates the task documents and carries out the work. It follows that project's task directory convention; without one, documents go under `docs/tasks/`. To resume, invoke `/lap.task` with the task name or its directory.

The skill is available across projects for that OS account. Installing it on a second machine installs the workflow, not your conversations, task journals, or approvals. To continue the same task elsewhere, commit the task documents in the project repository and clone or pull that project too. Each machine needs its own account access and permissions.

Update the skill deliberately:

```sh
git -C ~/.claude/skills/lap.task pull --ff-only
```

To remove it, move the `lap.task` directory outside the skills directory and start a new Claude session. If you enabled the optional hook below, remove that hook entry too.

## Permissions

There are separate decisions:

| Decision | Who controls it |
| --- | --- |
| Read a public copy of this repository | GitHub permits public cloning; no write access is needed. |
| Install this skill locally | The OS account running the clone must be able to write its own skills directory. |
| Approve a task's implementation scope | You, in the Claude conversation. |
| Read/write project files or run commands | Claude Code's permissions, working directories, sandbox, managed policies, and your OS account. |
| Push project changes, publish, or deploy | That machine's authenticated account and any required action approval. |

This skill does not set `allowed-tools`, add permission rules, enable a bypass mode, change sandbox settings, or install credentials. It is explicit-only: Claude loads it when you invoke it. Inspect or adjust the current host permissions with `/permissions`; approving the plan does not override them. A permission granted on your machine is not transferred by cloning this repo.

The definition approval rule is an instruction to the agent, not an OS-level file lock. The optional hook supplies a reminder; it cannot verify a conversation's approval or enforce every possible way of editing a file.

## Optional definition reminder

The workflow works without a hook or Python. To retain a reminder before Claude's `Edit` or `Write` tool changes an existing task definition, Python 3 must be available and you must explicitly install the hook.

Review `hooks/definition-reminder.py`, then merge this entry into the `hooks.PreToolUse` array in your Claude settings. Preserve any existing settings and hooks. Replace the command's path with the absolute path to your clone on that machine:

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

The script reads hook input, checks for an existing `definition.md` beside `progress.md`, and emits context. It writes no files, makes no network requests, and issues no permission decision. Hooks execute as local programs under your OS account; they are separate from the model's normal tool approval flow. Enabling this hook is optional and cloning alone does not enable it.

## Using the same workflow in Codex

The shared workflow is a standard skill at `skills/lap-task`. Install that directory through Codex's skill installer or copy it into `~/.agents/skills/lap-task`, then invoke `$lap-task`. Its display name is `lap.task`; the portable skill identifier uses hyphens. The Claude adapter at the repository root supplies the `/lap.task` command without duplicating the workflow.

## Origin and behavior

Adapted from BloomGameClient's `.claude/skills/task` workflow under the MIT license. The export keeps research, signoff, task documents, historical progress, and owner-confirmed completion. It replaces Bloom-specific file paths, logging APIs, and language limits with the current project's instructions. Definitions may be amended with explicit owner approval, consistent with the source project's current rules and reminder hook. The optional reminder uses Claude's structured context output rather than claiming to lock a file.

The existing Bloom `/task` remains separate. Claude Code's built-in `/tasks` manages background activity and is a different feature.

Official references: [Claude skills and installation](https://code.claude.com/docs/en/skills), [Claude permissions](https://code.claude.com/docs/en/permissions), [Claude hooks](https://code.claude.com/docs/en/hooks), [Codex skills](https://learn.chatgpt.com/docs/build-skills).
