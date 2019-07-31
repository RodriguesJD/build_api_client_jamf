from core.get_jamf.healthcarelistener import Healthcarelistener


def test_healthcarelistener():
    assert Healthcarelistener.status_code == 200

