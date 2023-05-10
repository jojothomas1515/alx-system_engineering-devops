#!/usr/bin/puppet apply

$nginx_conf="server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        add_header X-Served-By \$HOSTNAME always;

        error_page 404 /not_found.html;


        location / {
                try_files \$uri \$uri/ =404;
        }

        location /redirect_me {
                return 301 https://jojoport.netlify.com;
        }

        location = /not_found.html {
          internal;
        }
}"


package {'nginx':
  ensure   => installed,
  provider => 'apt',
}

file {'index.html':
  ensure   => file,
  path     => '/var/www/html/index.html',
  content  => 'Hello World!',
}

file {'not_found.html':
  ensure   => file,
  content  => "Ceci n'est pas une page",
  path     => '/var/www/html/not_found.html',
}

file {'default':
  ensure   => file,
  content  => $nginx_conf,
  path     => '/etc/nginx/sites-available/default',
  require  => Package['nginx'],
  notify   => Service['nginx'],
}

# run nginx service after install

service {'nginx':
  ensure  => 'running',
}
