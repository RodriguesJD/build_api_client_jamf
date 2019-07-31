from core.get_jamf.users import Users


def test_users():
    assert Users.status_code == 200

