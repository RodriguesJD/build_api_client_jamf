from core.get_jamf.printers import Printers


def test_printers():
    assert Printers.status_code == 200

