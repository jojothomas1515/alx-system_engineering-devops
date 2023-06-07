include stdlib

file_line {'fixing_type':
  ensure => present,
  path   => '/var/www/html/wp-settings.php',
  line   => 'php',
  match  => 'phpp',
}
