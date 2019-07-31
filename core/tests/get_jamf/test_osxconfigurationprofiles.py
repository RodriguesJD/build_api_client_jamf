from core.get_jamf.osxconfigurationprofiles import Osxconfigurationprofiles


def test_osxconfigurationprofiles():
    assert Osxconfigurationprofiles.status_code == 200

