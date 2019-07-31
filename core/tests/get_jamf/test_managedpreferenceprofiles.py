from core.get_jamf.managedpreferenceprofiles import Managedpreferenceprofiles


def test_managedpreferenceprofiles():
    assert Managedpreferenceprofiles.status_code == 200

