import math

def is_valid_speed(speed):
    if type(speed) not in (int, float):
        return False
    if not math.isfinite(speed):
        return False
    if speed < 0:
        return False

    return True

def is_valid_bounding_box(bounding_box):
    if not isinstance(bounding_box, tuple) or len(bounding_box) != 4:
        return False
    if not all(type(item) in (int, float) and math.isfinite(item) for item in bounding_box):
        return False
    if bounding_box[2] <= bounding_box[0] or bounding_box[3] <= bounding_box[1]:
        return False

    return True

def is_valid_status(status):
    if status in ("moving", "stationary", "unknown"):
        return True

    return False

def is_valid_id(vehicle_id):
    if type(vehicle_id) is not int:
        return False
    if vehicle_id < 0:
        return False

    return True

def is_valid_vehicle_type(vehicle_type):
    if not isinstance(vehicle_type, str):
        return False
    return vehicle_type in ("car", "truck", "bus", "motorcycle", "unknown")
