# Replace the number of workers from 4 to 10
# Restart nginx server

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
