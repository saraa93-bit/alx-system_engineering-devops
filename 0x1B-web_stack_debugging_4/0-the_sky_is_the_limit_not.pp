# bring ULIMIT higher
file { 'nginx_ulimit_settings':
  ensure  => file,
  path    => '/etc/default/nginx',
  content => "# Note: You may want to look at the following page before setting the ULIMIT.\n# http://wiki.nginx.org/CoreModule#worker_rlimit_nofile\n# Set the ulimit variable if you need defaults to change.\n# Example: ULIMIT=\"-n 4096\"\nULIMIT=\"-n 4096\"",
}

exec { 'restat-nginx':
    command => 'nginx restart',
    path    => '/etc/init.d/'
}
