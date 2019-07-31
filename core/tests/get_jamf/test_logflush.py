from core.get_jamf.logflush import Logflush


def test_logflush():
    assert Logflush.status_code == 200

