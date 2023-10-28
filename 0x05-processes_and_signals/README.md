# 0x05. Processes and signals project:
This directory of files for the 0x05. Processes and signals project
All the files and directory is described here
If any file or directory that is not described may be for testing purposes


`0-what-is-my-pid` -> a Bash script that displays its own PID.


`1-list_your_processes` -> a Bash script that displays a list of currently running processes.

- Must show all processes, for all users, including those which might not have a TTY
- Display in a user-oriented format
- Show process hierarchy


`2-show_your_bash_pid` -> Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:
- You cannot use pgrep
- The third line of your script must be # shellcheck disable=SC2009


`3-show_your_bash_pid_made_easy` -> a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.


`4-to_infinity_and_beyond` -> a Bash script that displays To infinity and beyond indefinitely.
In between each iteration of the loop, add a sleep 2


`5-dont_stop_me_now` -> a Bash script that stops `4-to_infinity_and_beyond` process.


`6-stop_me_if_you_can` -> a Bash script that stops `4-to_infinity_and_beyond` process.
You cannot use kill or killall


`7-highlander` -> a Bash script that displays:
- To infinity and beyond indefinitely
- With a sleep 2 in between each iteration
- I am invincible!!! when receiving a SIGTERM signal


`8-beheaded_process` -> a Bash script that kills the process 7-highlander.
