# `0x0C-web_server` project:

This directory of files for the 0x0C. Web server project
All the files and directory is described here
If any file or directory that is not described may be for testing purposes


`0-transfer_file` -> a Bash script that transfers a file from our client to a server:

Requirements:

- Accepts 4 parameters
	- The path to the file to be transferred
	- The IP of the server we want to transfer the file to
	- The username scp connects with
	- The path to the SSH private key that scp uses
- Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
- scp must transfer the file to the user home directory ~/
- Strict host key checking must be disabled when using scp
