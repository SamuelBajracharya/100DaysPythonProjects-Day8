from contact_dictionary import contact_dictionary


def main():
    end_program = False
    while not end_program:
        create_menu()
        choice = input("Enter your choice: ")
        contact_dictionary(choice)
        if choice == "6":
            end_program = True


def create_menu():
    print("Menu:")
    print("1. View all contacts.")
    print("2. Search a contact form the dictionary.")
    print("3. Add a new contact to the dictionary.")
    print("4. Edit a contact to the dictionary.")
    print("5. Remove a contact to the dictionary.")
    print("6. Exit the program")
    print("Please select an option from the menu above.")


if __name__ == "__main__":
    main()
