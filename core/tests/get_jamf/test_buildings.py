from core.get_jamf.buildings import Buildings


def test_buildings():
    assert Buildings.status_code == 200

