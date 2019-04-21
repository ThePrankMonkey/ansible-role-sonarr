import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sonarr_service(host):
    host.service('sonarr').is_running


def test_sonarr_page(host):
    cmd = host.run("curl 127.0.0.1:8989")
    cmd.rc == 0
    "Sonarr" in cmd.stdout
