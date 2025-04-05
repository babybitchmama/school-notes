#!/usr/bin/bash

set -e
SESSION_NAME="School Notes"

tmuxAttachCommand=""
if [ "$TMUX" != "" ]; then
  tmuxAttachCommand="tmux switch-client -t \"$SESSION_NAME:1\""
else
  tmuxAttachCommand="tmux attach -t \"$SESSION_NAME:1\""
fi

if tmux has-session -t "$SESSION_NAME" 2> /dev/null; then
  eval "$tmuxAttachCommand"
fi

tmux new-session -d -s "$SESSION_NAME"

# source ./todo-list/.tmux

#######################################################################
#                                                                     #
#                               College                               #
#                                                                     #
#######################################################################

############
#  Year 1  #
############

# source ./College/Year-1/fall/.tmux
# source ./College/Year-1/winter/.tmux
# source ./College/Year-1/spring/.tmux

############
#  Year 2  #
############

# source ./College/Year-2/fall/.tmux
# source ./College/Year-2/winter/.tmux
# source ./College/Year-2/spring/.tmux

#######################################################################
#                                                                     #
#                             University                              #
#                                                                     #
#######################################################################

############
#  Year 1  #
############

source ./University/Year-1/fall/.tmux
tmux new-window -t "$SESSION_NAME"

source ./University/Year-1/winter/.tmux
tmux new-window -t "$SESSION_NAME"

source ./University/Year-1/spring/.tmux
tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "DRP"
tmux send-keys -t "$SESSION_NAME" "cd ./University/Year-1/winter/drp/; clear" Enter

tmux new-window -t "$SESSION_NAME"

############
#  Year 2  #
############

# source ./University/Year-2/fall/.tmux
# source ./University/Year-2/winter/.tmux
# source ./University/Year-2/spring/.tmux

tmux rename-window -t "$SESSION_NAME" "Git"
tmux send-keys -t "$SESSION_NAME" "clear; wgs" Enter

tmux split-window -v

tmux send-keys -t "$SESSION_NAME" "clear" Enter
tmux send-keys -t "$SESSION_NAME" "g aa; g ce; g p; c"

eval "$tmuxAttachCommand"
