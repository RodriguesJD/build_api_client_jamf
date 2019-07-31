from core.get_jamf.activationcode import Activationcode


def test_activationcode():
    assert Activationcode.status_code == 200

