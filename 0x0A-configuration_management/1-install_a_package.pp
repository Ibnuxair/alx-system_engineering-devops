# Puppet Manifest to install Flask version 2.1.0
# and compatible Werkzeug using pip3

package { 'python3-pip':
ensure => installed,
}

exec { 'install_flask':
command => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.0.2',
path    => ['/usr/bin', '/usr/local/bin'],
unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
require => Package['python3-pip'],
}
