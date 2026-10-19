import math

def is_valid_speed(speed: object) -> bool:
    if not isinstance(speed, (int, float)) or isinstance(speed, bool):
        return False
    if isinstance(speed, float) and not math.isfinite(speed):
        return False
    if speed < 0:
        return False

    return True

def is_valid_bounding_box(bounding_box: object) -> bool:
    if not isinstance(bounding_box, tuple) or len(bounding_box) != 4:
        return False
    if not all(
        not isinstance(item, bool) and(
            isinstance(item, int)
            or isinstance(item, float)
            and math.isfinite(item)
        )
        for item in bounding_box
    ):
        return False
    if bounding_box[2] <= bounding_box[0] or bounding_box[3] <= bounding_box[1]:
        return False

    return True

def is_valid_status(status: object) -> bool:
    if status in ("moving", "stationary", "unknown"):
        return True

    return False

def is_valid_id(vehicle_id: object) -> bool:
    if type(vehicle_id) is not int:
        return False
    if vehicle_id < 0:
        return False

    return True

def is_valid_vehicle_type(vehicle_type: object) -> bool:
    if not isinstance(vehicle_type, str):
        return False
    return vehicle_type in ("car", "truck", "bus", "motorcycle", "unknown")
