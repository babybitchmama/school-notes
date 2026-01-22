#!/usr/bin/bash

tmux rename-window -t "$SESSION_NAME" "MTH-410"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/winter/mth-410/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-432"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/winter/mth-432/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-445"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/winter/mth-445/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "PHYS-483"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/winter/phys-483/; clear" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "DRP 26"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/winter/drp/; clear" Enter

tmux new-window -t "$SESSION_NAME"
