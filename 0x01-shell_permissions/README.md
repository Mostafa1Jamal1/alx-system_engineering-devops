0-iam_betty > is an executable file that switches the current user to the user betty

1-who_am_i > is an executable file that prints the effective username of the current user.

2-groups > is an executable file that prints all the groups the current user is part of.

3-new_owner > is an executable file that changes the owner of the file hello to the user betty.

4-empty > is an executable file that creates an empty file called hello.

5-execute > is an executable file that adds execute permission to the owner of the file hello.

6-multiple_permissions > is an executable file that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

7-everybody > is an executable file that adds execution permission to the owner, the group owner and the other users, to the file hello.

8-James_Bond > is an executable file that sets the permission to the file hello as follows:
- Owner: no permission at all
- Group: no permission at all
- Other users: all the permissions

9-John_Doe > is an executable file that sets the mode of the file hello to this:
-rwxr-x-wx

10-mirror_permissions > is an executable file that sets the mode of the file hello the same as olleh’s mode.

11-directories_permissions > is an executable file that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.

12-directory_permissions > is an executable file that creates a directory called my_dir with permissions 751 in the working directory.

13-change_group > is an executable file that changes the group owner to school for the file hello.

100-change_owner_and_group > is an executable file that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

101-symbolic_link_permissions > is an executable file that changes the owner and the group owner of _hello to vincent and staff respectively.

102-if_only > is an executable file that changes the owner of the file hello to betty only if it is owned by the user guillaume.
