# Let’s practice using Puppet to make changes to our configuration file.
# Just as in the previous configuration file task, we’d like you to set
# up your client SSH configuration file so that you can connect to a server
# without typing a password.

# Requirements:
#     Your SSH client configuration must be configured to use the private key `~/.ssh/school`
#     Your SSH client configuration must be configured to refuse to authenticate using a password

# ensure private key exists
file {'~/.ssh/school':
  ensure => file
}

# Turn off passwd auth
exec {'Turn off passwd auth':
  command  => 'echo "    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  provider => 'shell'
}

# Declare identity file
exec {'Declare identity file':
  command  => 'echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  provider => 'shell'
}
