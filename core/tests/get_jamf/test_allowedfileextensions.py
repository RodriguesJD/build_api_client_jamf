from core.get_jamf.allowedfileextensions import Allowedfileextensions


def test_allowedfileextensions():
    assert Allowedfileextensions.status_code == 200

