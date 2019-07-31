from core.get_jamf.computercheckin import Computercheckin


def test_computercheckin():
    assert Computercheckin.status_code == 200

