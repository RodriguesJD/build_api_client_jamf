from core.get_jamf.webhooks import Webhooks


def test_webhooks():
    assert Webhooks.status_code == 200

