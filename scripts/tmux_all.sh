#!/usr/bin/env bash
set -euo pipefail

SESSION_NAME="${1:-leetcode-all}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"

python -m pip install -r requirements.txt

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
echo
echo "Cancel:"
echo "  tmux kill-session -t $SESSION_NAME"
echo "Cancel all tmux sessions:"
echo "  tmux kill-server"
