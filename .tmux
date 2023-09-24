#!/usr/bin/bash

set -e
SESSION_NAME="School Notes"

tmuxAttachCommand=""
if [ "$TMUX" != "" ]; then
  tmuxAttachCommand="tmux switch-client -t \"$SESSION_NAME:MTH-253\""
else
  tmuxAttachCommand="tmux attach -t \"$SESSION_NAME:MTH-253\""
fi

if tmux has-session -t "$SESSION_NAME" 2> /dev/null; then
  eval "$tmuxAttachCommand"
fi

tmux new-session -d -s "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-253"
tmux send-keys -t "$SESSION_NAME" "cd ./College/Year-1/spring/mth-253/; clear; lanc" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "PHY-123"
tmux send-keys -t "$SESSION_NAME" "cd ./College/Year-1/spring/phy-123/; clear; lanc" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "PSY-202A"
tmux send-keys -t "$SESSION_NAME" "cd ./College/Year-1/spring/psy-202a/; clear; lanc" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "Git"
tmux send-keys -t "$SESSION_NAME" "clear; watch git status" Enter

eval "$tmuxAttachCommand"
