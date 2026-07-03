#!/usr/bin/env bash
set -euo pipefail

SESSION_NAME="${1:-leetcode-all}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"

tmux new-session -d -s "$SESSION_NAME" \
  "PYTHONPATH=src python scripts/generate_solutions.py"

echo "Started tmux session: $SESSION_NAME"
echo
echo "View sessions:"
echo "  tmux ls"
echo
echo "Attach:"
echo "  tmux attach -t $SESSION_NAME"
echo
echo "Cancel:"
echo
echo "  tmux kill-server"
