import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
  os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_cloudflare_credentials(host):
    f = host.file('/etc/certbot-dns-cloudflare-credentials.ini')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_certbot_install(host):
    pkg = host.package('certbot')
    assert pkg.is_installed
