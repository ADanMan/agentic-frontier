#!/bin/bash
# Daily wrapper: draft the AI digest, then fire a macOS notification reminder.
# Meant to be run by a launchd LaunchAgent (see scripts/install_reminder.sh),
# but safe to run by hand too.
#
# It only DRAFTS the digest — it never commits. You review and commit yourself.

set -euo pipefail

REPO_DIR="$HOME/Desktop/agentic-frontier"
cd "$REPO_DIR"

# Prefer python3 from PATH; fall back to common location.
PYTHON_BIN="$(command -v python3 || echo /usr/bin/python3)"

"$PYTHON_BIN" scripts/digest.py >>"$REPO_DIR/.digest.log" 2>&1 || true

# macOS notification so you don't forget to write + commit today.
osascript -e 'display notification "Draft ready in digests/ — curate & commit your TIL." with title "agentic-frontier" sound name "Glass"' || true
