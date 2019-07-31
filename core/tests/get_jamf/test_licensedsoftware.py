from core.get_jamf.licensedsoftware import Licensedsoftware


def test_licensedsoftware():
    assert Licensedsoftware.status_code == 200

