from core.get_jamf.computergroups import Computergroups


def test_computergroups():
    assert Computergroups.status_code == 200

