# a manifest that kills a process named killmenow.

exec { 'pkill killmenow':
  cwd  => '/usr/bin',
  path => '/usr/bin'
}
