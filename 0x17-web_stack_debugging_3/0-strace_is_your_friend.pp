# Puppet script that fixes whole typo errors in php files
exec { '/var/www/html/wp-setting.php':
  path    => '/usr/local/bin:/bin/',
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
