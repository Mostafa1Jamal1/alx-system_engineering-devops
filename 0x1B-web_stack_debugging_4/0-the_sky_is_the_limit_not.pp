# fix our stack so that we get to 0 failing requests

exec { 'fix our stack':
  command => 'sed -i 's/worker_processes [1-5];/worker_processes 6;/' /etc/nginx/nginx.conf'
}
