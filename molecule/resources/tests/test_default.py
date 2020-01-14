import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_libreoffice_installed(host):
    libreoffice = host.package("libreoffice")

    assert libreoffice.is_installed


def test_libreoffice_path_set(host):
    path = host.environment()["PATH"]
    assert "/opt/libreoffice/program/soffice" in path


def test_libreoffice_version(host):
    libreoffice_version = host.run("soffice --version")

    assert libreoffice_version.rc == 0
    assert 'LibreOffice 5.3.6.1 30(Build:1)' in libreoffice_version.stdout
