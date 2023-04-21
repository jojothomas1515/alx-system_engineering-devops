file { '/tmp/school':
   mode     => '0744',
  checksum => 'md5',
  owner    => 'www-data',
  group    => 'www-data',
  content  => 'I love Puppet',
  }
