#!/bin/bash
# http://stackoverflow.com/questions/2575037/how-to-get-the-cursor-position-in-bash
# http://unix.stackexchange.com/questions/88296/get-vertical-cursor-position

# based on a script from http://invisible-island.net/xterm/xterm.faq.html

exec < /dev/tty
oldstty=$(stty -g)
stty raw -echo min 0
# on my system, the following line can be replaced by the line below it
echo -en "$1\033[6n" > /dev/tty
# tput u7 > /dev/tty
# tput u7 > /dev/tty    # when TERM=xterm (and relatives)
IFS=';' read -r -d R -a pos
stty $oldstty
# change from one-based to zero based so they work with: tput cup $row $col
row=$((${pos[0]:2} - 1))    # strip off the esc-[
col=$((${pos[1]} - 1))


echo ":$row:$col"
