from core.get_jamf.smtpserver import Smtpserver


def test_smtpserver():
    assert Smtpserver.status_code == 200

