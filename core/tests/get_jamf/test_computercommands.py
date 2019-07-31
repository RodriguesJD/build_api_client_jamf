from core.get_jamf.computercommands import Computercommands


def test_computercommands():
    assert Computercommands.status_code == 200

