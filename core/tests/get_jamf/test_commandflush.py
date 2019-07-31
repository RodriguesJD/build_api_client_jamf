from core.get_jamf.commandflush import Commandflush


def test_commandflush():
    assert Commandflush.status_code == 200

