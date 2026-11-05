#!/usr/bin/env python3
"""Optional Claude Code reminder; never grants or denies tool permission."""

import json
import sys
from pathlib import Path

DEFINITION_NAME = "definition.md"
PROGRESS_NAME = "progress.md"
FILE_TOOLS = {"Edit", "Write"}


def reminder(event):
    if event.get("tool_name") not in FILE_TOOLS:
        return {}
    target = Path(event["tool_input"]["file_path"])
    if not target.is_absolute():
        target = Path(event["cwd"]) / target
    if target.name != DEFINITION_NAME or not target.is_file():
        return {}
    if not target.with_name(PROGRESS_NAME).is_file():
        return {}
    return {"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "additionalContext": (
            "lap.task: This is an existing task definition. Change it only if "
            "the owner explicitly approved this amendment; record the reason "
            "and approval in progress.md. Otherwise preserve the definition "
            "and record discoveries in progress.md. This reminder does not "
            "verify approval or grant tool permission."
        ),
    }}


if __name__ == "__main__":
    print(json.dumps(reminder(json.load(sys.stdin))))
