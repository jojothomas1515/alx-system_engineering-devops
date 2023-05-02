# install and configure nginx using puppet

$conf = "server{
  listen 80 default_server;
  listen [::]:80;
  index index.html index.htm index.nginx-debian.html;

  server_name _;

  error_page 404 /not_found.html;

  location /redirect_me {
    return 301 https://jojoport.netlify.com;
    }
  location / {
    try_files \$uri \$uri/ =404;
  }
  
  }"

  $not_found = "Ceci n'est pas une page"

  package {'nginx':
    ensure   => installed,
    provider => apt,
  }
 file {'index.html':
    ensure   => file,
    checksum => 'md5',
    content  => 'Hello World!',
    path     => '/var/www/html/index.html',
    require  => Package['nginx'],
  }

  file {'not_found.html':
    ensure   => file,
    checksum => 'md5',
    content  => $not_found,
    path     => '/var/www/html/not_found.html'
    require  => Package['nginx'],
  } 

  service {'nginx':
    ensure => running,
  }

  file {'default':
    ensure   => file,
    checksum => 'md5',
    content  => $conf,
    path     => '/etc/nginx/sites-available/default',
    require  => Package['nginx'],
    notify   => Service['nginx'],
  }
