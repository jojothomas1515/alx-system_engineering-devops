$nginx_conf = "
         add_header X-Served-By \$HOSTNAME always;
         error_page 404 /not_found.html;
         location /redirect_me {
           return 301 https://jojoport.netlify.com;
         }"


package {'nginx':
  ensure   => latest,
  provider => 'apt',
}

# run nginx service after install

service {'nginx':
  ensure  => 'running',
}

file {'index.html':
  ensure  => file,
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

file {'not_found.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
  path    => '/var/www/html/not_found.html',
}

file_line {'default':
  ensure  => present,
  after   => 'server_name _;',
  line    => $nginx_conf,
  path    => '/etc/nginx/sites-available/default',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
