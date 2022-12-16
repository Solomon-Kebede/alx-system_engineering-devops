# Time to practice configuring your server with Puppet!
# Just as you did before, we’d like you to install and
# configure an Nginx server using Puppet instead of Bash.
# To save time and effort, you should also include
# resources in your manifest to perform
# a 301 redirect when querying /redirect_me.

# Requirements:
#     -Nginx should be listening on port 80
#     -When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must
#		return a page that contains the string `Hello World!`
#     -The redirection must be a "301 Moved Permanently"
#     -Your answer file should be a Puppet manifest containing commands to automatically configure an
#		Ubuntu machine to respect above requirements


# execute 'apt-get update'
exec {'apt-update':
  command => '/usr/bin/apt-get update -y'
}

# install nginx package (sudo apt-get install -y nginx)
package {'nginx':
  ensure  => installed,
  require => Exec['apt-update'],
  provider=> 'apt',
}

# modify directory permissions
exec {'/var/www':
  command => '/usr/bin/sudo /usr/bin/chmod -R 777 /var/www',
  path    => '/var/www/',
}

# create home page @ index.html
exec {'create home page':
  require => Exec['/var/www'],
  command => '/usr/bin/echo "Hello World!" > /var/www/html/index.html',
}

# modify nginx configuration file
exec {'modify nginx config':
  require => Exec['/var/www'],
  command => '/usr/bin/sudo /usr/bin/sed -i s/"listen \[::\]:80 default_server;"/"listen \[::\]:80 default_server;\n\tlocation \/redirect_me {rewrite \/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent; return 301;}\n\n\terror_page 404 \/custom_404.html;\n\tlocation = \/custom_404.html {root \/var\/www\/html;internal;}\n"/g "/etc/nginx/sites-available/default"',
  path    => '/etc/nginx/sites-available/',
}

# restart nginx
exec {'nginx restart':
  require => Exec['modify nginx config'],
  command => '/usr/bin/sudo /usr/sbin/nginx',
}

