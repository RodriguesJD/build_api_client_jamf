from core.get_jamf.patchsoftwaretitles import Patchsoftwaretitles


def test_patchsoftwaretitles():
    assert Patchsoftwaretitles.status_code == 200

