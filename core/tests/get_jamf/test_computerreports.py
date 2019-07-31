from core.get_jamf.computerreports import Computerreports


def test_computerreports():
    assert Computerreports.status_code == 200

