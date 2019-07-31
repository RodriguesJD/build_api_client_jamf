from core.get_jamf.mobiledeviceapplications import Mobiledeviceapplications


def test_mobiledeviceapplications():
    assert Mobiledeviceapplications.status_code == 200

