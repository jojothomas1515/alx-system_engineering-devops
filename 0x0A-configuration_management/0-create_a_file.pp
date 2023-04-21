# create a file named school in the temp folder
file { '/tmp/school':
  ensure   => file,
  checksum => 'md5',
  content  => 'I love Puppet',
  mode     => '0744',
  owner    => 'www-data',
  group    => 'www-data',
  }
