# remove the limit of open files for holberton user

exec { 'remove limit':
  command => 'sed -i "/holberton/d" /etc/security/limits.conf'
}
