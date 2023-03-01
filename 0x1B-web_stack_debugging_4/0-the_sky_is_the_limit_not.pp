#  Sky is the limit, let's bring that limit higher 

exec { 'fix-sky-limit':
  command => 'sed -i "s/15/4096/g" /etc/default/nginx',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',

}

exec { 'restart-nginx':
  command => 'service nginx restart',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  require => Exec['fix-sky-limit'],
}
