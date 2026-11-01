from logging_config import configure_logging
from vehicle.processor import Vehicle
import json
from vehicle.validator import is_valid_speed, is_valid_id, is_valid_vehicle_type

def save_vehicle_data(vehicle_id: int, vehicle_type: str) -> None:
    with open("vehicles.txt", "a") as file:
        file.write(f"Vehicle ID: {vehicle_id}\n")
        file.write(f"Vehicle Type: {vehicle_type}\n")

def load_vehicle_data(file_name: str) -> str:
    try:
        with open(file_name, "r") as file:
            content = file.read()
            return content

    except FileNotFoundError as error:
        raise FileNotFoundError("File does not exist: Please enter a valid path") from error
    except PermissionError as error:
        raise PermissionError("File can't be accessed: Please check file permission") from error
    except IsADirectoryError as error:
        raise IsADirectoryError("Can't open directory as file: Please check file path") from error

def save_vehicle_json(vehicle_id: int, vehicle_type: str, vehicle_speed: float | None) -> None:
    vehicle_data = {
        "vehicle_id": vehicle_id,
        "vehicle_type": vehicle_type,
        "vehicle_speed": vehicle_speed
    }

    with open("vehicle.json", "w") as file:
        json.dump(vehicle_data, file, indent = 4)

def load_vehicle_json(file_name: str) -> dict[str, object]:
    try:
        with open(file_name, "r") as file:
            required_fields = {"vehicle_id", "vehicle_type", "vehicle_speed"}
            content = json.load(file)
            if not isinstance(content, dict):
                    raise ValueError("Expected a JSON object")
            missing_fields = required_fields - content.keys()
            if missing_fields:
                raise ValueError(f"Missing required fields: {missing_fields}")
            if not is_valid_speed(content["vehicle_speed"]):
                raise ValueError("Invalid speed")
            if not is_valid_vehicle_type(content["vehicle_type"]):
                raise ValueError("Invalid Vehicle Type: Vehicle Type must be in (\"car\", \"truck\", \"bus\", \"motorcycle\", \"unknown\")")
            if not is_valid_id(content["vehicle_id"]):
                raise ValueError("Invalid Vehicle ID: Vehicle ID must be non-negative integer")
            return content
    except FileNotFoundError as error:
        raise FileNotFoundError("File does not exist: Please enter a valid path") from error
    except PermissionError as error:
        raise PermissionError("File can't be accessed: Please check file permission") from error
    except IsADirectoryError as error:
        raise IsADirectoryError("Can't open directory as file: Please check file path") from error
    except json.JSONDecodeError as error:
        raise ValueError(
            "Invalid JSON content: Please check the file"
        ) from error



def main():
    data = load_vehicle_json("vehicle.json")
    print(data)



if __name__ == "__main__":
    main()
