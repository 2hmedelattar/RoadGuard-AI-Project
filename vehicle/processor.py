from .validator import is_valid_speed, is_valid_bounding_box, is_valid_status, is_valid_id, is_valid_vehicle_type

class Vehicle:

    def __init__(self, vehicle_id, vehicle_type, bounding_box):

        # Main attributes for any vehicle in our system
        if is_valid_id(vehicle_id):
            self._vehicle_id = vehicle_id
        else:
            raise ValueError("Invalid Vehicle ID: Vehicle ID must be non-negative integer")

        if is_valid_vehicle_type(vehicle_type):
            self._vehicle_type = vehicle_type
        else:
            raise ValueError("Invalid Vehicle Type: Vehicle Type must be in (\"car\", \"truck\", \"bus\", \"motorcycle\", \"unknown\")")

        if is_valid_bounding_box(bounding_box):
            self._bounding_box = bounding_box
        else:
            raise ValueError("Invalid bounding box: X2 must be greater than X1 and Y2 must be greater than Y1")

        # Initialize speed and movement status as not yet measured or analyzed
        self._current_speed = None
        self._status = None

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @property
    def vehicle_type(self):
        return self._vehicle_type

    @property
    def bounding_box(self):
        return self._bounding_box

    @property
    def current_speed(self):
        return self._current_speed

    @property
    def status(self):
        return self._status

    def update_speed(self, new_speed):

        # Updating vehicle speed with the new speed
        if new_speed is None:
            self._current_speed = None
        elif is_valid_speed(new_speed):
            self._current_speed = new_speed
        else:
            raise ValueError("Invalid speed")

    def update_status(self, new_status):

        # Updating vehicle status with the new status
        if is_valid_status(new_status):
            self._status = new_status
        else:
            raise ValueError("Invalid status: status must be one of these (\"unknown\", \"moving\", \"stationary\")")

    def update_bounding_box(self, new_bounding_box):

        # Updating vehicle bounding box with the new bounding box
        if is_valid_bounding_box(new_bounding_box):
            self._bounding_box = new_bounding_box
        else:
            raise ValueError("Invalid bounding box: X2 must be greater than X1 and Y2 must be greater than Y1")

    def update_vehicle_type(self, new_vehicle_type):
        if is_valid_vehicle_type(new_vehicle_type):
            self._vehicle_type = new_vehicle_type
        else:
            raise ValueError("Invalid Vehicle Type: Vehicle Type must be in (\"car\", \"truck\", \"bus\", \"motorcycle\", \"unknown\")")
