from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'', 'ck1e.urls', name=' '),
    host(r'layout', 'layout.urls', name='layout'),
)
