import datetime

def load_initial_data():
    cars = {
        "CAR001": {"type": "SUV", "available": True},
        "CAR002": {"type": "Sedan", "available": True},
        "CAR003": {"type": "Hatchback", "available": True}
    }
    users = ["user1", "user2"]
    rentals = {}
    return cars, users, rentals

def display_menu():
    print("\n--- Car Rental System ---")
    print("1. View Available Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")
    return input("Enter your choice: ")

def view_available_cars(cars):
    print("\nAvailable Cars:")
    for car_id, details in cars.items():
        if details["available"]:
            print(f"{car_id} - {details['type']}")
    log_event("Viewed available cars")

def rent_car(cars, users, rentals):
    user_id = input("Enter your user ID: ")
    if user_id not in users:
        print("Invalid user.")
        return

    view_available_cars(cars)
    car_id = input("Enter Car ID to rent: ")

    if car_id in cars and cars[car_id]["available"]:
        cars[car_id]["available"] = False
        rentals[user_id] = car_id
        print(f"{user_id} rented {car_id}")
        log_event(f"{user_id} rented {car_id}")
    else:
        print("Car not available or invalid ID.")
        log_event(f"{user_id} failed to rent {car_id}")

def return_car(cars, rentals):
    user_id = input("Enter your user ID: ")
    if user_id in rentals:
        car_id = rentals[user_id]
        cars[car_id]["available"] = True
        del rentals[user_id]
        print(f"{user_id} returned {car_id}")
        log_event(f"{user_id} returned {car_id}")
    else:
        print("No rental record found.")
        log_event(f"{user_id} attempted return with no rental")

def log_event(message):
    log_message = f"{datetime.datetime.now()} - {message}\n"
    