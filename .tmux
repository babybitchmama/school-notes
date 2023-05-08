#!/usr/bin/bash

set -e
SESSION_NAME="School Notes"

if tmux has-session -t="$SESSION_NAME" 2> /dev/null; then
  tmux attach -t "$SESSION_NAME"
  exit
fi

tmux new-session -d -s "$SESSION_NAME"

tmux rename-session "$SESSION_NAME"

tmux rename-window "MTH-253"
tmux send-keys "cd ./College/Year-2/spring/mth-253/; clear" Enter

tmux new-window

tmux rename-window "PHY-123"
tmux send-keys "cd ./College/Year-2/spring/phy-123/; clear" Enter

tmux new-window

tmux rename-window "PSY-202A"
tmux send-keys "cd ./College/Year-2/spring/psy-202a/; clear" Enter

tmux attach -t "$SESSION_NAME:MTH-253"
