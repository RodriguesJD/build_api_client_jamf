from core.get_jamf.categories import Categories


def test_categories():
    assert Categories.status_code == 200

