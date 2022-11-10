exec { 'from_4_to_10-workers':
  command  => "sed -i s/'worker_processes 4'/'worker_processes 10'/g /etc/nginx/nginx.conf",
  provider => 'shell',
  user     => 'root'
}

exec { 'service nginx restart':
  command  => 'service nginx restart',
  provider => 'shell',
  user     => 'root'
}
