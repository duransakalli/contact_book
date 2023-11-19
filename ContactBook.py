# ContactBook Application

def add_contact(contact_book):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    contact_book[name] = {'phone': phone, 'email': email}
    print("Contact added!\n\n")


def view_contact(contact_book):
    for name, details in contact_book.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
        print("\n")


def update_contact(contact_book):
    name = input("Enter the contact name to update: ")
    if name in contact_book:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contact_book[name] = {'phone': phone, 'email': email}
        print("Contact updated! \n\n")
    else:
        print("Contact not fount! \n\n")


def delete_contact(contact_book):
    name = input("Enter the contact name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted! \n\n")
    else:
        print("Contact not fount! \n\n")


def main():
    contact_book = {}
    while True:
        print("\n")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")
        print("\n")

        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contact(contact_book)
        elif choice == '3':
            update_contact(contact_book)
        elif choice == '4':
            delete_contact(contact_book)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid input. Try again.\n")


if __name__ == '__main__':
    main()
