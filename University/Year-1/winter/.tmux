#!/usr/bin/bash

tmux rename-window -t "$SESSION_NAME" "MTH-282"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/winter/mth-282/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-342"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/winter/mth-342/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-317"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/winter/mth-317/; clear" Enter
