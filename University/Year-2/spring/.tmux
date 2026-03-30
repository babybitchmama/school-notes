#!/usr/bin/bash

tmux rename-window -t "$SESSION_NAME" "MTH-446"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/spring/mth-446/; clear" Enter

tmux new-window -t "$SESSION_NAME"
