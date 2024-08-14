exec { 'Fix wordpress site':
  command   => 'sed -i "s/oldtext/newtext/" /c/Apache24/htdocs/wordpress/wp-config.php',
  provider  => 'shell',
  onlyif    => 'test -f /c/Apache24/htdocs/wordpress/wp-config.php',
}
