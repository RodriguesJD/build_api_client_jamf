from core.get_jamf.restrictedsoftware import Restrictedsoftware


def test_restrictedsoftware():
    assert Restrictedsoftware.status_code == 200

