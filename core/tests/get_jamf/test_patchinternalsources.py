from core.get_jamf.patchinternalsources import Patchinternalsources


def test_patchinternalsources():
    assert Patchinternalsources.status_code == 200

