from vehicle.validator import is_valid_speed

def main():

    speed = 85
    result = is_valid_speed(speed)
    print(f"Is Valid Speed ? {result}")

if __name__ == "__main__":
    main()
