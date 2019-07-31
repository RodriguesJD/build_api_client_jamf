from core.get_jamf.peripherals import Peripherals


def test_peripherals():
    assert Peripherals.status_code == 200

