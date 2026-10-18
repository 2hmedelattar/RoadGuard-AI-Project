from vehicle.validator import is_valid_speed
from vehicle.processor import Vehicle

def main():

    vehicle_1 = Vehicle(
        vehicle_id = 15,
        vehicle_type = "car",
        bounding_box = (100, 150, 300, 400)
    )

    try:
        vehicle_1.update_bounding_box((300, 400, 100, 200))
        print(vehicle_1.bounding_box)
    except ValueError as error:
        print("Invalid bounding box: X2 must be greater than X1 and Y2 must be greater than Y1")
    print(vehicle_1.bounding_box)

    try:
        vehicle_2 = Vehicle(
                vehicle_id = 15,
                vehicle_type = "car",
                bounding_box = (300, 400, 100, 200)
            )
    except ValueError as error:
        print("Invalid bounding box: X2 must be greater than X1 and Y2 must be greater than Y1")


if __name__ == "__main__":
    main()
