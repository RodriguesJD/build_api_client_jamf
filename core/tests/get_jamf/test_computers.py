from core.get_jamf.computers import Computers


def test_computers():
    assert Computers.status_code == 200

