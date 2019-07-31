from core.get_jamf.scripts import Scripts


def test_scripts():
    assert Scripts.status_code == 200

