from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, update_user, add_course, search_course_by_id, search_course_by_user_name

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Update User by ID") 
    print("6. Add Course")
    print("7. Search Course by ID")
    print("8. Search Course by User Name")
    print("9. Exit")

def main():
    create_table() 
    while True:
        menu()
        choice = input("Select an option (1-9): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            user_id = int(input("Enter user ID to update: "))
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            update_user(user_id, name, email)
        elif choice == '6':
            course_name = input("Enter course name: ")
            unit = int(input("Enter course unit: "))
            add_course(course_name, unit)
        elif choice == '7':
            course_id = int(input("Enter ID to search: "))
            search_course_by_id(course_id)
        elif choice == '8':
            user_name = input("Enter user name to search courses: ")
            search_course_by_user_name(user_name)
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
