from core.get_jamf.byoprofiles import Byoprofiles


def test_byoprofiles():
    assert Byoprofiles.status_code == 200

