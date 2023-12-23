# 0x0A. Configuration management project:
This directory of files for the 0x0A. Configuration management project
All the files and directory is described here
If any file or directory that is not described may be for testing purposes


`0-create_a_file.pp` -> Using Puppet, create a file in /tmp.

Requirements:

File path is /tmp/school
File permission is 0744
File owner is www-data
File group is www-data
File contains I love Puppet


`1-install_a_package.pp` -> Using Puppet, install flask from pip3.

Requirements:

Install flask
Version must be 2.1.0


`2-execute_a_command.pp` -> a manifest that kills a process named killmenow.

Requirements:

use the exec Puppet resource
use pkill
