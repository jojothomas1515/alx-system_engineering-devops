# exec a command to kill a program

exec {'pkill killmenow':
  onlyif   => 'test `pgrep killmenow`',
  provider => 'shell',
  }
