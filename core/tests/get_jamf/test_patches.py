from core.get_jamf.patches import Patches


def test_patches():
    assert Patches.status_code == 200

