# `command_line_for_the_win`


This is a project to learn about SFTP, what is it?, how to use it and other things.
Also to improve the shell manipulation skills there is a chalange to solve.


# How to use SFTP:

There is couple of ways to do the same thing so if you seen other way no problem.

- > Using the sftp command:
> sftp `username``@``hostname`
- Then a passwoed required to proceed 

Now there should be a sftp prompt looks like this:
sftp> 
"Duh"

You can navigate almost like the way you navigate in your shell by using commands like:
`cd` -> to change the working directory
`pwd` -> tp print the current working directory
`ls` -> to list the contents of the current working directory
and so on..

You can see all the available command by using the help command:
sftp> help

Now as simple as `mv` command, use the `put` command to uploud a file
to the current working directory in the remote system

sftp> put the_file_to_uploud a_new_name_if_wanted


tadah
