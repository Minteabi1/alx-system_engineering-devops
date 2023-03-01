# user limit

exec {'user limit':
  command  => 'sudo sed -i \'s/nofile 4/nofile 10000/\' /etc/security/limits.conf',
  provider => shell,

}

exec {'user soft':
  command  => 'sudo sed -i \'s/nofile 4/nofile 10000/\' /etc/security/limits.conf',
  provider => shell,

}