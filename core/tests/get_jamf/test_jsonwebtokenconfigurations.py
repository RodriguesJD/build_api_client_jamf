from core.get_jamf.jsonwebtokenconfigurations import Jsonwebtokenconfigurations


def test_jsonwebtokenconfigurations():
    assert Jsonwebtokenconfigurations.status_code == 200

