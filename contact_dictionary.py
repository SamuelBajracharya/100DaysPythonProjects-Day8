contacts = {}


def view_all_contacts():
    if not contacts:
        print("No items in the contact dictionary")

    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Email: {details['email']}")
        print(f"Phone: {details['phone']}")


def search_contact():
    search_input = input("Enter name of contact to search: ")
    if search_input in contacts:
        print("User found: ")
        print(f"Name: {search_input}")
        print(f"Email: {contacts[search_input]['email']}")
        print(f"Phone: {contacts[search_input]['phone']}")
    else:
        print(f"Contact of Name: {search_input} not found.")


def add_new_contact():
    name = input("Enter name of contact: ")
    email = input("Enter email of contact: ")
    phone = input("Enter phone of contact: ")

    contacts[name] = {"email": email, "phone": phone}
    print("Contact added to the contact dictionary.")


def edit_contact():
    if not contacts:
        print("No item to edit in contacts")
    name = input("Enter name of contact to edit: ")
    if name in contacts:
        email = input("Enter updated email: ")
        phone = input("Enter updated phone: ")
        contacts[name] = {"email": email, "phone": phone}
        print("Contact successfully updated.")
    else:
        print(f"Contact of Name: {name} not found.")


def remove_contact():
    if not contacts:
        print("No item to remove in contacts")
    name = input("Enter name of contact to remove: ")
    if name in contacts:
        del contacts[name]
        print(f"Successfully deleted the contact with name: {name}")
    else:
        print(f"Contact of Name: {name} not found.")


choices = {
    "1": view_all_contacts,
    "2": search_contact,
    "3": add_new_contact,
    "4": edit_contact,
    "5": remove_contact,
}


def contact_dictionary(choice):
    action = choices[choice]
    if action:
        action()

    else:
        print("Invalid choice. Please try again.")
