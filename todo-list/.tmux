#!/usr/bin/bash

tmux rename-window -t "$SESSION_NAME" "MTH-251"
tmux send-keys -t "$SESSION_NAME" "cd ./College/Year-1/fall/mth-251/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-252"
tmux send-keys -t "$SESSION_NAME" "cd ./College/Year-1/winter/mth-252/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-253"
tmux send-keys -t "$SESSION_NAME" "cd ./College/Year-1/spring/mth-253/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-254"
tmux send-keys -t "$SESSION_NAME" "cd ./College/Year-2/winter/mth-254/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-261"
tmux send-keys -t "$SESSION_NAME" "cd ./College/Year-2/fall/mth-261/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-256"
tmux send-keys -t "$SESSION_NAME" "cd ./College/Year-2/spring/mth-256/; clear" Enter
