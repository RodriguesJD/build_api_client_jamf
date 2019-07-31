from core.get_jamf.accounts import Accounts


def test_accounts():
    assert Accounts.status_code == 200

