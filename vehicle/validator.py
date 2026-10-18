def is_valid_speed(speed):
    return speed >= 0

def is_valid_bounding_box(bounding_box):
    if (isinstance(bounding_box, tuple) or isinstance(bounding_box, list)) and len(bounding_box) == 4:
        if all(isinstance(item, (int, float)) for item in bounding_box):
            if bounding_box[2] > bounding_box[0] and bounding_box[3] > bounding_box[1]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

