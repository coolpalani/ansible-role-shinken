import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('component', [
    'poller',
    'scheduler',
    'broker',
    'receiver',
    'reactionner',
    'arbiter',
])
def test_services_running(Service, component):
    s = Service('shinken-' + component)
    assert s.is_running
    assert s.is_enabled
