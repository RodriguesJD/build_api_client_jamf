from core.get_jamf.ebooks import Ebooks


def test_ebooks():
    assert Ebooks.status_code == 200

