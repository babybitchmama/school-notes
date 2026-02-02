#!/usr/bin/bash

tmux rename-window -t "$SESSION_NAME" "MTH-407"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/fall/mth-407/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-431"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/fall/mth-431/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-444"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/fall/mth-444/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-461"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/fall/mth-461/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-687"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/fall/mth-637/; clear" Enter

tmux new-window -t "$SESSION_NAME"
