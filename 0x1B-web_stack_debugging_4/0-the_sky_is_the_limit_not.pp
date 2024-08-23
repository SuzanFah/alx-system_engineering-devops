# This Puppet manifest configures Nginx to handle high traffic more effectively.

exec { 'fix--for-nginx':
  command => '/usr/sbin/nginx -s reload',
  path    => ['/usr/sbin', '/usr/bin'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
