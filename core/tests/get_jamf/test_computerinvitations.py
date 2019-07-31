from core.get_jamf.computerinvitations import Computerinvitations


def test_computerinvitations():
    assert Computerinvitations.status_code == 200

