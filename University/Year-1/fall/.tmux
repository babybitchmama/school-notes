#!/usr/bin/bash

tmux rename-window -t "$SESSION_NAME" "MTH-281"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/fall/mth-281/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-307"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/fall/mth-307/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-316"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/fall/mth-316/; clear" Enter
