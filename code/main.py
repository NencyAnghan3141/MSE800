from user_manager import UserManager
from car_inventory import CarInventory
from booking_service import BookingService

def main():
    user_manager = UserManager()
    car_inventory = CarInventory()
    booking_service = BookingService()
    current_user = None

    while True:
        print("\n--- Car Rental System ---")
        print("1. Register")
        print("2. Login")
        print("3. Add Car (Admin)")
        print("4. Update Car (Admin)")
        print("5. Delete Car (Admin)")
        print("6. List Available Cars")
        print("7. Create Booking")
        print("8. Approve Booking (Admin)")
        print("9. Reject Booking (Admin)")
        print("10. View My Bookings and Charges (Customer)")
        print("11. Exit")


        choice = input("Enter choice: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            role = input("Role (customer/admin): ")
            user_manager.register_user(username, password, role)
            print("User registered.")

        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")
            user = user_manager.authenticate_user(username, password)
            if user:
                print(f"Welcome, {user[1]} ({user[3]})")
                current_user = user
            else:
                print("Invalid credentials.")

        elif choice == '3':
            if current_user and current_user[3] == 'admin':
                make = input("Car make: ")
                model = input("Car model: ")
                year = int(input("Year: "))
                mileage = int(input("Mileage: "))
                min_days = int(input("Min rental days: "))
                max_days = int(input("Max rental days: "))
                car_id = car_inventory.add_new_car(make, model, year, mileage, min_days, max_days)
                print(f"Car {car_id} added.")
            else:
                print("Admin access only.")

        elif choice == '4':
            if current_user and current_user[3] == 'admin':
                car_id = input("Enter Car ID to update: ")
                make = input("New make: ")
                model = input("New model: ")
                year = int(input("New year: "))
                mileage = int(input("New mileage: "))
                min_days = int(input("New min rental days: "))
                max_days = int(input("New max rental days: "))
                car_inventory.update_car(car_id, make, model, year, mileage, min_days, max_days)
                print("Car updated.")
            else:
                print("Admin access only.")

        elif choice == '5':
            if current_user and current_user[3] == 'admin':
                car_id = input("Enter Car ID to delete: ")
                car_inventory.delete_car(car_id)
                print("Car deleted.")
            else:
                print("Admin access only.")

        elif choice == '6':
            cars = car_inventory.get_available_cars()
            for car in cars:
                print(f"ID: {car[0]}, {car[1]} {car[2]} ({car[3]}) - Mileage: {car[4]} km")

        elif choice == '7':
            if current_user:
                car_id = input("Enter Car ID: ")
                start = input("Start date (YYYY-MM-DD): ")
                end = input("End date (YYYY-MM-DD): ")
                booking_id = booking_service.create_booking(current_user[0], car_id, start, end)
                if booking_id:
                    print(f"Booking {booking_id} created.")
            else:
                print("Login required.")

        elif choice == '8':
            if current_user and current_user[3] == 'admin':
                booking_id = input("Enter Booking ID to approve: ")
                booking_service.approve_booking(booking_id)
                print("Booking approved.")
            else:
                print("Admin access only.")

        elif choice == '9':
            if current_user and current_user[3] == 'admin':
                booking_id = input("Enter Booking ID to reject: ")
                booking_service.reject_booking(booking_id)
                print("Booking rejected.")
            else:
                print("Admin access only.")


        elif choice == '10':
            if current_user and current_user[3] == 'customer':
                bookings = booking_service.get_user_bookings(current_user[0])
                if bookings:
                    print("\nYour Bookings:")
                    for booking in bookings:
                        print(f"Booking ID: {booking[0]}, Car ID: {booking[1]}, Start: {booking[2]}, End: {booking[3]}, Status: {booking[4]}, Fee: ${booking[5]:.2f}")
                else:
                    print("No bookings found.")
            else:
                print("Customer access only.")


        elif choice == '11':
            break
if __name__ == "__main__":
    main()
