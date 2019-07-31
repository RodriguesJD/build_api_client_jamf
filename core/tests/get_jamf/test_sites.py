from core.get_jamf.sites import Sites


def test_sites():
    assert Sites.status_code == 200

