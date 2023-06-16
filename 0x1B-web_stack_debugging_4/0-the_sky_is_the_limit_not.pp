# update the limit

service {'nginx':
  ensure  => running,
  restart => 'service nginx restart',
  }

exec {'limit':
  command => 'sed -i "/^ULIMIT/d" /etc/default/nginx',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
  notify  => Service['nginx'],
  }
