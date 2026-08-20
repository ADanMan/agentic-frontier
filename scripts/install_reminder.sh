#!/bin/bash
# OPTIONAL: install a daily macOS reminder (09:30) that drafts the digest and
# pops a notification so you don't forget to write + commit.
#
# This is a *user* LaunchAgent — no sudo, no system changes. Run it only if you
# want the reminder. To remove it later, run this script with `uninstall`.
#
#   bash scripts/install_reminder.sh            # install (default 09:30)
#   bash scripts/install_reminder.sh 08:00      # install at a custom HH:MM
#   bash scripts/install_reminder.sh uninstall  # remove it

set -euo pipefail

LABEL="com.adanman.agentic-frontier-digest"
PLIST="$HOME/Library/LaunchAgents/${LABEL}.plist"
WRAPPER="$HOME/Desktop/agentic-frontier/scripts/daily_digest.sh"

if [[ "${1:-}" == "uninstall" ]]; then
  launchctl unload "$PLIST" 2>/dev/null || true
  rm -f "$PLIST"
  echo "Removed reminder ($LABEL)."
  exit 0
fi

# Parse HH:MM (default 09:30).
TIME="${1:-09:30}"
HOUR="${TIME%%:*}"
MINUTE="${TIME##*:}"

mkdir -p "$HOME/Library/LaunchAgents"
chmod +x "$WRAPPER"

cat >"$PLIST" <<PLIST_EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${LABEL}</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${WRAPPER}</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>${HOUR#0}</integer>
        <key>Minute</key>
        <integer>${MINUTE#0}</integer>
    </dict>
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
PLIST_EOF

launchctl unload "$PLIST" 2>/dev/null || true
launchctl load "$PLIST"

echo "Installed daily reminder at ${TIME} (label: ${LABEL})."
echo "It drafts digests/ and shows a macOS notification. It never commits."
echo "Remove with: bash scripts/install_reminder.sh uninstall"
