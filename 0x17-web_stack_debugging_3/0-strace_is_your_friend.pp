# 1-handle_500_errors.pp
# Puppet manifest to handle Apache 500 error

# Install Apache2 package (if not already installed)
package { 'apache2':
  ensure => installed,
}

# Ensure Apache is running
service { 'apache2':
  ensure => running,
}

# Configure Apache to display more detailed error messages
file { '/etc/apache2/conf-available/display_errors.conf':
  ensure  => present,
  content => "LogLevel debug\nServerSignature Off\n",
}

# Enable the new configuration
exec { 'enable_display_errors_conf':
  command     => 'a2enconf display_errors',
  path        => '/usr/bin:/bin',
  refreshonly => true,
  subscribe   => File['/etc/apache2/conf-available/display_errors.conf'],
  require     => Package['apache2'],
}

# Restart Apache to apply changes
service { 'apache2':
  ensure    => running,
  subscribe => Exec['enable_display_errors_conf'],
  require   => Package['apache2'],
}