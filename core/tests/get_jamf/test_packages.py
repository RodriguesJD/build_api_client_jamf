from core.get_jamf.packages import Packages


def test_packages():
    assert Packages.status_code == 200

