from core.get_jamf.vppaccounts import Vppaccounts


def test_vppaccounts():
    assert Vppaccounts.status_code == 200

