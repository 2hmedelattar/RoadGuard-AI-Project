import pytest
from vehicle.processor import Vehicle

@pytest.fixture
def valid_vehicle():
    return Vehicle(
        vehicle_type = "car",
        vehicle_id = 15,
        bounding_box = (10, 20, 100, 200)
    )

def test_update_speed_invalid_value(valid_vehicle):
    valid_vehicle.update_speed(50)
    with pytest.raises(ValueError):
        valid_vehicle.update_speed(-10)

    assert valid_vehicle.current_speed == 50

@pytest.mark.parametrize(
    "vehicle_id, vehicle_type, bounding_box",
    [
        (-1, "car", (10, 20, 100, 200)),
        (15, "bicycle", (10, 20, 100, 200)),
        (15, "car", (100, 20, 10, 200)),
    ]
)
def test_vehicle_constructor_rejects_invalid_data(
    vehicle_id, vehicle_type, bounding_box
):
    with pytest.raises(ValueError):
        Vehicle(
            vehicle_type = vehicle_type,
            vehicle_id = vehicle_id,
            bounding_box = bounding_box
        )

def test_vehicle_constructor_accepts_valid_data(valid_vehicle):
    assert valid_vehicle.vehicle_id == 15
    assert valid_vehicle.vehicle_type == "car"
    assert valid_vehicle.bounding_box == (10, 20, 100, 200)
