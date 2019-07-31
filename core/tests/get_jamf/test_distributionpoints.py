from core.get_jamf.distributionpoints import Distributionpoints


def test_distributionpoints():
    assert Distributionpoints.status_code == 200

