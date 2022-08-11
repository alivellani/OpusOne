import pytest

import powercalc


def test_hash_values():
    """Test """

    # how willt his be inhertied, how to get this data to be dynamic
    data = {"Voltage": 240.0, "Amps": 1.5}
    assert powercalc.hash_values(data) == (240.0, 1.5, 0.9)

    data = {"Volts": 4160, "Current": 25, "PF": 0.75}
    assert powercalc.hash_values(data) == (4160, 25, 0.75)

def test_iter_dict():
    data = {
    "Empty House": {"V": 120.0, "I": 0.0},
    "My House": {"V": 120.0, "i": 4.5},
    "Your House": {"v": 124.0, "I": 3.78},
    "240 House": {"Voltage": 240.0, "Amps": 1.5},
    "Light Commercial": {"V": 600.0, "I": 1.5},
    "Large Commercial": {"V": 600.0, "Amperes": 15.5},
    "Industrial #1": {"Volts": 4160, "Current": 25, "PF": 0.75},
    "Industrial #2": {"Volts": 4160, "Current": 30, "PF": 0.95}
}

    assert powercalc.iter_dict(data)

def test_incorrect_iter_dict():
    wrong_data = {
        "Empty House": {"V": 120.0, "I": 0.0},
        "My House": {"V": 120.0, "i": 4.5},
        "Your House": {"vo": 124.0, "I": 3.78},
        "240 House": {"Voltage": 240.0, "Amps": 1.5},
        "Light Commercial": {"V": 600.0, "I": 1.5},
        "Large Commercial": {"V": 600.0, "Amperes": 15.5},
        "Industrial #1": {"Volts": 4160, "Current": 25, "PF": 0.75},
        "Industrial #2": {"Volts": 4160, "Current": 30, "PF": 0.95}
    }

    with pytest.raises(Exception) as e_info:
        assert powercalc.iter_dict(wrong_data)


