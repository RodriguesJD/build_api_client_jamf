from core.get_jamf.vppinvitations import Vppinvitations


def test_vppinvitations():
    assert Vppinvitations.status_code == 200

