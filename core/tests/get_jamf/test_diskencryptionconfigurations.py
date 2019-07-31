from core.get_jamf.diskencryptionconfigurations import Diskencryptionconfigurations


def test_diskencryptionconfigurations():
    assert Diskencryptionconfigurations.status_code == 200

