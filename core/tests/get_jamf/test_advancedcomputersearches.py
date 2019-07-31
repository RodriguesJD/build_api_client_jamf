from core.get_jamf.advancedcomputersearches import Advancedcomputersearches


def test_advancedcomputersearches():
    assert Advancedcomputersearches.status_code == 200

