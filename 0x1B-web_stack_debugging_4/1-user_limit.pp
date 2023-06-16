# remove holberton user limit

exec {'remove limit for holberton':
  command  => 'sed -i "/holberton/d" /etc/security/limits.conf'
  provider => shell,
  }
