augeas{"Turn off passwd auth" :
  context => "/etc/ssh/ssh_config",
  changes => "set PasswordAuthentication no",
}


augeas{"Declare identity file" :
  context => "/etc/ssh/ssh_config",
  changes => "set IdentityFile ~/.ssh/school",
}

