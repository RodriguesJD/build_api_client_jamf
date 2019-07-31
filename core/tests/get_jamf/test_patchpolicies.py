from core.get_jamf.patchpolicies import Patchpolicies


def test_patchpolicies():
    assert Patchpolicies.status_code == 200

