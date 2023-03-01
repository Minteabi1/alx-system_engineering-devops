# using Strace to debug a program

exec {'fix-wordp':
    provider => shell,
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
aLJzzYDnP5D832d