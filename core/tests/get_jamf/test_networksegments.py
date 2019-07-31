from core.get_jamf.networksegments import Networksegments


def test_networksegments():
    assert Networksegments.status_code == 200

