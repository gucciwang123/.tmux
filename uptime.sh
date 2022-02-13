boot=0
now=$(cut -d'.' -f1 < /proc/uptime)
# shellcheck disable=SC1004

uptime=$(( now - boot ))
y=$(( uptime / 31536000 ))
dy=$(( uptime / 86400 % 365 ))
d=$(( uptime / 86400 ))
h=$(( uptime / 3600 % 24))
m=$(( uptime / 60 % 60 ))
s=$(( uptime % 60 ))

tmux set -g @uptime_y $y
tmux set -g @uptime_dy $dy
tmux set -g @uptime_d $d
tmux set -g @uptime_h $h
tmux set -g @uptime_m $m
tmux set -g @uptime_s $s

printf " %dd %02d:%02d" ${d} ${h} ${m}

