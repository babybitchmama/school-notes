#!/usr/bin/bash

tmux rename-window -t "$SESSION_NAME" "MTH-433"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/spring/mth-433/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-411"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/spring/mth-411/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "CS-410"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/spring/cs-410/; clear" Enter
