from core.get_jamf.advancedusersearches import Advancedusersearches


def test_advancedusersearches():
    assert Advancedusersearches.status_code == 200

