from core.get_jamf.gsxconnection import Gsxconnection


def test_gsxconnection():
    assert Gsxconnection.status_code == 200

