# find out why Apache is returning a 500 error cause of .phpp extensions

exec { 'fix-extention':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
