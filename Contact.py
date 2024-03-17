contacts = {}

def add_contact(name, phone, email, address):
    contacts[name] = {'phone': phone, 'email': email, 'address': address}

def view_contacts():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}")

def search_contact(keyword):
    results = []
    for name, info in contacts.items():
        if keyword.lower() in name.lower() or keyword in info['phone']:
            results.append((name, info))
    return results

def update_contact(name, phone, email, address):
    if name in contacts:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def display_contact(name):
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"Address: {info['address']}")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            add_contact(name, phone, email, address)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = search_contact(keyword)
            if results:
                print("Search results:")
                for name, info in results:
                    print(f"Name: {name}, Phone: {info['phone']}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            if name in contacts:
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                update_contact(name, phone, email, address)
            else:
                print("Contact not found.")

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()

