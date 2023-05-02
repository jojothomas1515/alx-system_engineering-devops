$conf = "
HOST *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
"



file {'config':
  ensure   => file,
  content  => $conf,
  checksum => 'md5',
  path     => '~/.ssh/config',
}
