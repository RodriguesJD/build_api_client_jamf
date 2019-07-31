from core.get_jamf.patchexternalsources import Patchexternalsources


def test_patchexternalsources():
    assert Patchexternalsources.status_code == 200

