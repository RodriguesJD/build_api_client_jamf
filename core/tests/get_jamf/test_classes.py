from core.get_jamf.classes import Classes


def test_classes():
    assert Classes.status_code == 200

