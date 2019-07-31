from core.get_jamf.savedsearches import Savedsearches


def test_savedsearches():
    assert Savedsearches.status_code == 200

