from core.get_jamf.mobiledevicegroups import Mobiledevicegroups


def test_mobiledevicegroups():
    assert Mobiledevicegroups.status_code == 200

