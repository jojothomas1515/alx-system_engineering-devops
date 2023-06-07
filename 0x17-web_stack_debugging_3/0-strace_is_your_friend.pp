service {'apache2':
  ensure  => running,
  enable  => true,
  restart => true,
  }

exec {'sub phpp for php':
  command => 'sed -i "s/phpp/php/" wp-settings.php',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
  notify  => Service['apache2'],
  }
