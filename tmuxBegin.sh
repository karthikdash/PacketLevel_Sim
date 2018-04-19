#!/bin/sh
tmux new-session -d 'python multicommodity.py 0.001'
tmux split-window -h 'python multicommodity.py 0.003'
tmux select-pane -t 0
tmux split-window -h 'python multicommodity.py 0.002'
tmux select-pane -t 2
tmux split-window -h 'python multicommodity.py 0.004'
tmux select-pane -t 0
tmux split-window -v 'python multicommodity.py 0.005'
tmux select-pane -t 2
tmux split-window -v 'python multicommodity.py 0.006'
tmux select-pane -t 4
tmux split-window -v 'python multicommodity.py 0.007'
tmux select-pane -t 6
tmux split-window -v 'python multicommodity.py 0.008'
tmux select-pane -t 7
tmux split-window -v' python multicommodity.py 0.009'
tmux attach-session -d
