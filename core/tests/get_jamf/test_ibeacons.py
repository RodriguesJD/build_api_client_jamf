from core.get_jamf.ibeacons import Ibeacons


def test_ibeacons():
    assert Ibeacons.status_code == 200

