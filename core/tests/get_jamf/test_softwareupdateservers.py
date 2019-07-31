from core.get_jamf.softwareupdateservers import Softwareupdateservers


def test_softwareupdateservers():
    assert Softwareupdateservers.status_code == 200

