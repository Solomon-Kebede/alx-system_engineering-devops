# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
#   The name of the custom HTTP header must be X-Served-By
#   The value of the custom HTTP header must be the hostname of the server Nginx is running on
#   Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task


# execute 'apt-get update'
exec { 'apt-update':
  command  => '/usr/bin/sudo /usr/bin/apt-get update',
  provider => 'shell'
}

# install nginx package
package { 'nginx':
  require => Exec['apt-update'],
}

# set directory permissions for file writing
exec { 'chmod-/var/www':
  require  => Package['nginx'],
	command  => '/usr/bin/sudo /usr/bin/chmod -R 777 /var/www',
	provider => 'shell'
}

# create homepage
file { '/var/www/html/index.html':
  require => Exec['chmod-/var/www'],
  ensure  => file,
  content => "Hello World!"
}

# start nginx service
exec { 'nginx-start':
  require  => File['/var/www/html/index.html'],
	command  => '/usr/bin/sudo /usr/sbin/nginx',
	provider => 'shell'
}

# edit server response header
exec { 'edit-header':
  require  => Exec['nginx-start'],
	command  => '/usr/bin/sudo /usr/bin/sed -i "s/404;/404;add_header X-Served-By $(uname -n);/g" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# restart nginx service
exec { 'nginx-restart':
  require  => Exec['edit-header'],
  command  => '/usr/bin/sudo /usr/sbin/nginx -s stop; /usr/bin/sudo /usr/sbin/nginx',
	provider => 'shell'
}
