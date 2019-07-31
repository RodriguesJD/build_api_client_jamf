from core.get_jamf.mobiledevices import Mobiledevices


def test_mobiledevices():
    assert Mobiledevices.status_code == 200

