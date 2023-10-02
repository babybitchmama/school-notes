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

source ./College/Year-2/fall/.tmux
# source ./College/Year-2/winter/.tmux
# source ./College/Year-2/spring/.tmux

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "Git"
tmux send-keys -t "$SESSION_NAME" "clear; wgs" Enter

eval "$tmuxAttachCommand"
