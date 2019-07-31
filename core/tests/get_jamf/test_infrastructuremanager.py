from core.get_jamf.infrastructuremanager import Infrastructuremanager


def test_infrastructuremanager():
    assert Infrastructuremanager.status_code == 200

