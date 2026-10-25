from .validator import is_valid_speed, is_valid_bounding_box, is_valid_status, is_valid_id, is_valid_vehicle_type
import logging

logger = logging.getLogger("roadguard.vehicle.processor")

class Vehicle:

    def __init__(self, vehicle_id: int, vehicle_type: str, bounding_box: tuple[int | float, int | float, int | float, int | float]) -> None:

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
        self._current_speed: int | float | None = None
        self._status: str | None = None

    @property
    def vehicle_id(self) -> int:
        return self._vehicle_id

    @property
    def vehicle_type(self) -> str:
        return self._vehicle_type

    @property
    def bounding_box(self) -> tuple[int | float, int | float, int | float, int | float]:
        return self._bounding_box

    @property
    def current_speed(self) -> int | float | None:
        return self._current_speed

    @property
    def status(self) -> str | None:
        return self._status

    def update_speed(self, new_speed: int | float | None) -> None:

        # Updating vehicle speed with the new speed
        if new_speed is None:
            self._current_speed = None
            logger.warning(
                "Vehicle speed measurement unavailable | vehicle_id = %s | current_speed = %s",
                self._vehicle_id,
                self._current_speed
            )
        elif is_valid_speed(new_speed):
            self._current_speed = new_speed
            logger.info(
                "Vehicle speed updated | vehicle_id = %s | speed = %s",
                self._vehicle_id,
                new_speed
            )
        else:
            logger.error(
                "Vehicle speed is invalid | vehicle_id = %s | received_speed = %r | current_speed = %s",
                self._vehicle_id,
                new_speed,
                self._current_speed
            )
            raise ValueError("Invalid speed")

    def update_status(self, new_status: str) -> None:

        # Updating vehicle status with the new status
        if is_valid_status(new_status):
            self._status = new_status
        else:
            raise ValueError("Invalid status: status must be one of these (\"unknown\", \"moving\", \"stationary\")")

    def update_bounding_box(self, new_bounding_box: tuple[int | float, int | float, int | float, int | float]) -> None:

        # Updating vehicle bounding box with the new bounding box
        if is_valid_bounding_box(new_bounding_box):
            self._bounding_box = new_bounding_box
        else:
            raise ValueError("Invalid bounding box: X2 must be greater than X1 and Y2 must be greater than Y1")

    def update_vehicle_type(self, new_vehicle_type: str) -> None:
        if is_valid_vehicle_type(new_vehicle_type):
            self._vehicle_type = new_vehicle_type
        else:
            raise ValueError("Invalid Vehicle Type: Vehicle Type must be in (\"car\", \"truck\", \"bus\", \"motorcycle\", \"unknown\")")
