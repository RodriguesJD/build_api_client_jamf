from core.get_jamf.macapplications import Macapplications


def test_macapplications():
    assert Macapplications.status_code == 200

