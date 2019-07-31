from core.get_jamf.jssuser import Jssuser


def test_jssuser():
    assert Jssuser.status_code == 200

