from core.get_jamf.directorybindings import Directorybindings


def test_directorybindings():
    assert Directorybindings.status_code == 200

