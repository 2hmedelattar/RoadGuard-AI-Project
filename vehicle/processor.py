from .validator import is_valid_speed, is_valid_bounding_box

class Vehicle:

    def __init__(self, vehicle_id, vehicle_type, bounding_box):

        # Main attributes for any vehicle in our system
        self._vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type

        if is_valid_bounding_box(bounding_box):
            self.bounding_box = bounding_box
        else:
            raise ValueError("Invalid bounding box: X2 must be greater than X1 and Y2 must be greater than Y1")
        
        # Initialize values as unknown 
        self.current_speed = None
        self.status = None

    @property
    def vehicle_id(self):
        return self._vehicle_id

    def update_speed(self, new_speed):

        # Updating vehicle speed with the new speed
        if is_valid_speed(new_speed):
            self.current_speed = new_speed
        else: 
            print("Error: Can't Update Vehicle Speed (Validation Purpose)")

    def update_status(self, new_status):

        # Updating vehicle status with the new status
        self.status = new_status

    def update_bounding_box(self, new_bounding_box):

        # Updating vehicle bounding box with the new bounding box
        if is_valid_bounding_box(new_bounding_box):
            self.bounding_box = new_bounding_box
        else:
            raise ValueError("Invalid bounding box: X2 must be greater than X1 and Y2 must be greater than Y1")
