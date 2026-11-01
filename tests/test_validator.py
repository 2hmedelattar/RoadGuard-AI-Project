import pytest

from vehicle.validator import (
    is_valid_bounding_box,
    is_valid_id,
    is_valid_speed,
    is_valid_vehicle_type,
)


@pytest.mark.parametrize(
    "vehicle_id, expected",
    [
        (15, True),
        (0, True),
        (-1, False),
        (1.5, False),
        ("15", False),
        (True, False),
    ],
)
def test_is_valid_id(vehicle_id, expected):
    assert is_valid_id(vehicle_id) is expected


@pytest.mark.parametrize(
    "vehicle_type, expected",
    [
        ("car", True),
        ("truck", True),
        ("bus", True),
        ("motorcycle", True),
        ("unknown", True),
        ("bicycle", False),
        ("", False),
        (15, False),
    ],
)
def test_is_valid_vehicle_type(vehicle_type, expected):
    assert is_valid_vehicle_type(vehicle_type) is expected


@pytest.mark.parametrize(
    "vehicle_speed, expected",
    [
        (15, True),
        (-1, False),
        (float("inf"), False),
        (float("nan"), False),
        (None, False),
        ("50", False),
        (0, True),
        (50.05, True),
        (True, False),
    ],
)
def test_is_valid_speed(vehicle_speed, expected):
    assert is_valid_speed(vehicle_speed) is expected


@pytest.mark.parametrize(
    "bounding_box, expected",
    [
        ((10, 20, 100, 200), True),
        ((10.5, 20.5, 100.5, 200.5), True),
        ((10, 20, 10, 200), False),
        ((10, 20, 100, 20), False),
        ((100, 20, 10, 200), False),
        ((10, 200, 100, 20), False),
        ((10, 20, 100), False),
        ([10, 20, 100, 200], False),
        ((10, 20, True, 200), False),
        ((10, 20, float("nan"), 200), False),
    ],
)
def test_is_valid_bounding_box(bounding_box, expected):
    assert is_valid_bounding_box(bounding_box) is expected
