#!/usr/bin/bash

tmux rename-window -t "$SESSION_NAME" "MTH-281"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/fall/mth-281/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-282"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/winter/mth-282/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-307"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/fall/mth-307/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-316"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/fall/mth-316/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-317"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/winter/mth-317/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-441"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/winter/mth-441/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-411"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/spring/mth-411/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-433"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/spring/mth-433/; clear" Enter
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

tmux rename-window -t "$SESSION_NAME" "MTH-637"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/fall/mth-637/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-410"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/winter/mth-410/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-432"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/winter/mth-432/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-445"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/winter/mth-445/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-638"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/winter/mth-638/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "PHYS-483"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/winter/phys-483/; clear" Enter
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "MTH-446"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-2/spring/mth-446/; clear" Enter
tmux new-window -t "$SESSION_NAME"
