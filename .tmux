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
tmux send-keys "cd ./College/Year-1/spring/mth-253/; clear; lanc" Enter

tmux new-window

tmux rename-window "PHY-123"
tmux send-keys "cd ./College/Year-1/spring/phy-123/; clear; lanc" Enter

tmux new-window

tmux rename-window "PSY-202A"
tmux send-keys "cd ./College/Year-1/spring/psy-202a/; clear; lanc" Enter

tmux new-window

tmux rename-window "Git"
tmux send-keys "clear; git status" Enter

tmux attach -t "$SESSION_NAME:MTH-253"
