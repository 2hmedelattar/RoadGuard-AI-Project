from logging_config import configure_logging
from vehicle.processor import Vehicle
def main():
    configure_logging()
    configure_logging()
    vehicle_1 = Vehicle(
        vehicle_id = 15,
        vehicle_type = "car",
        bounding_box = (100, 200, 300, 400)
    )
    vehicle_1.update_speed(15)
    vehicle_1.update_speed(0)
    vehicle_1.update_speed(None)


if __name__ == "__main__":
    main()
