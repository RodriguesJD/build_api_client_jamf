from core.get_jamf.netbootservers import Netbootservers


def test_netbootservers():
    assert Netbootservers.status_code == 200

