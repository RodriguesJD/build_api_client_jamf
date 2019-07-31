from core.get_jamf.departments import Departments


def test_departments():
    assert Departments.status_code == 200

