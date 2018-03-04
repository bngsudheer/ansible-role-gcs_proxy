import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_gsql_proxy_enabled(host):
    assert host.service('gcsql_proxy').is_enabled


def test_gcsql_proxy_user(host):
    assert host.user('gcsql_proxy') is not None
