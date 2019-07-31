from core.get_jamf.policies import Policies


def test_policies():
    assert Policies.status_code == 200

