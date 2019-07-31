from core.get_jamf.vppassignments import Vppassignments


def test_vppassignments():
    assert Vppassignments.status_code == 200

