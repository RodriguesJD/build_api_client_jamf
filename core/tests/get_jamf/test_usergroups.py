from core.get_jamf.usergroups import Usergroups


def test_usergroups():
    assert Usergroups.status_code == 200

