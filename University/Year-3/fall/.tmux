#!/usr/bin/bash

tmux rename-window -t "$SESSION_NAME" "MTH-616"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-3/fall/mth-616/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-410 (AI)"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-3/fall/mth-410/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-410 (Combinatorics)"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-3/fall/mth-4100/; clear" Enter

tmux new-window -t "$SESSION_NAME"
