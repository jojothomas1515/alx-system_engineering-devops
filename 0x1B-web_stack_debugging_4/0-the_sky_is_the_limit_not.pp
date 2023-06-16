# update the limit

service {'nginx':
  ensure  => running,
  enable  => true,
  restart => true,
  }

exec {'limit':
  command => 'sed -i "s/ULIMIT=\"-n 4096\"/ULIMIT=\"-n 4096\"" /etc/default/nginx',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
  notify  => Service['nginx'],
  }
