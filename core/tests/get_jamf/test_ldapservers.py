from core.get_jamf.ldapservers import Ldapservers


def test_ldapservers():
    assert Ldapservers.status_code == 200

