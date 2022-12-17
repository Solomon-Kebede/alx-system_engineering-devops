# execute 'apt-get update'
exec { 'apt-update':
  command  => '/usr/bin/sudo /usr/bin/apt-get update',
  provider => 'shell'
}

# install nginx package
package { 'nginx':
  require => Exec['apt-update'],
  ensure  => installed
}

# set directory permissions for file writing
exec { 'chmod /var/www':
  require  => Package['nginx'],
	command  => '/usr/bin/sudo /usr/bin/chmod -R 777 /var/www',
	provider => 'shell'
}

# create homepage
file { '/var/www/html/index.html':
  require => Exec['chmod /var/www'],
  ensure  => file,
  content => "Hello World!"
}

# start nginx service
service { 'nginx start':
  require  => File['/var/www/html/index.html'],
	ensure   => running,
	provider => 'service'
}

# edit server response header
exec { 'edit-header':
  require  => Service['nginx start'],
	command  => '/usr/bin/sudo /usr/bin/sed -i "s/404;/404;add_header X-Served-By $hostname;/g" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# restart nginx service
exec { 'nginx restart':
  require  => Exec['edit-headerx'],
  command  => '/usr/bin/sudo /usr/sbin/nginx -s stop; /usr/bin/sudo /usr/sbin/nginx'
	provider => 'shell'
}
