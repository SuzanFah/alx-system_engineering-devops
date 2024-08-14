# Example Puppet manifest for Windows
exec { 'Fix_wordpress_site':
  command => 'powershell.exe -Command "Write-Output \'Fixing WordPress site...\'"',
  path    => ['C:/Windows/System32', 'C:/Windows'],
}
