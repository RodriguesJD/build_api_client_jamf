from core.get_jamf.computerconfigurations import Computerconfigurations


def test_computerconfigurations():
    assert Computerconfigurations.status_code == 200

