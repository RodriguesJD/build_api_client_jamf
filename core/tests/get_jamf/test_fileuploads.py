from core.get_jamf.fileuploads import Fileuploads


def test_fileuploads():
    assert Fileuploads.status_code == 200

