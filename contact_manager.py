#Developer- Anand Sagar Rout
#Project Name- contact management system

import json
import re
from datetime import datetime
import csv

#Phone Number validation
def validate_phone(phone):
    '''This function help to check whether the phone number is valid or not.'''
    #remove all the non-digit character and replace with ''
    digits=re.sub(r'\D','',phone)

    #check the phone number is it in international standard format(10-15) digit or not ?
    if 10<=len(digits)<=15:
        return True,digits
    return False,None

def validate_email(email):
    '''This function check whether the given email correct or not '''
    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email) is not None


# ================= FILE HANDLING ================= #

def load_contacts():
    try:
        with open("contacts_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Warning: contacts file is corrupted. Starting fresh.")
        return {}

def save_contacts(contacts):
    with open("contacts_data.json", "w") as f:
        json.dump(contacts, f, indent=4)

#========================CRUD FUNCTION=========================================================
def add_contact(contacts):
    '''This Function add new contacts.'''
    print("----Add Contacts----")

    #input name of contact
    name=input("Enter The Name: ").strip().title()
    if not name:
        print("Name can't be empty.")
        return
    if name in contacts:
        print("This name already exists.")
        return
    
    #Input Phone number
    phone=input("Enter Phone Number: ")
    valid,phone=validate_phone(phone)
    if not valid:
        print("Please enter valid phone number!")
        return
    
    #Input email
    email=input("Enter your email: ").strip()
    if email and not validate_email(email):
        print("Please Enter Valid email.")
        return
    
    #Address and group input.
    address=input("Enter Your Address: ")
    group=input("Enter your Group: ")or "other"

    #Save the details
    contacts[name]={
        "Phone":phone,
        "Email":email,
        "group":group,
        "address":address,
        "Created at":datetime.now().isoformat(),
        "Updated at":datetime.now().isoformat()
    }

    print("Contact added successfully.")

    
#Display details of all contacts
def display_allcontacts(contacts):
    '''Dispaly the details of all contacts.'''

    print("----All contacts details.----")
    if not contacts:
        print("Empty contact list!")
        return
    
    for name,info in contacts.items():
        print(f"Name:{name}")
        print(f"Ph no.:{info['Phone']}")
        print(f"Email:{info['Email']}")
        print(f"address:{info['address']}")
        print(f"Groups:{info['group']}")

#Search Contact
def search_contact(contacts):
    '''Search Contact by their name'''
    term=input("Enter name for search: ").lower()
    found=False

    for name, info in contacts.items():
        if term in name.lower():
            print(f"\n{name} -> {info['Phone']}")
            found=True

    if not found:
        print("No matching contact found.")

#update a contact
def update_contacts(contacts):
    '''Update any contact.'''

    name=input("Enter the name want to upadate: ").title()

    if name not in contacts:
        print("Contact not found.")
        return
    
    # FIX: added .strip() and skip update if input is empty
    phone=input("Enter new phone (press Enter to skip): ").strip()
    if phone:
        valid,cleaned=validate_phone(phone)
        if valid:
            contacts[name]['Phone']=cleaned
        else:
            print("Invalid phone number. Keeping old value.")

    # FIX: skip update if input is empty
    email=input("Enter new email (press Enter to skip): ").strip()
    if email:
        if validate_email(email):
            contacts[name]['Email']=email
        else:
            print("Invalid email. Keeping old value.")

    contacts[name]['Updated at']=datetime.now().isoformat()
    print("Contact Updated.")

#Delete any contact
def delete_contact(contacts):
    '''Delete any contact.'''

    name=input("Enter name to be deleted: ").title()

    if name not in contacts:
        print("Contact not found.")
        return

    confirm=input("Are you sure?(y/n): ").lower()
    if confirm=='y':
        del contacts[name]
        print("Deleted Successfully!")

#============================Extra Features=============================================
def export_csv(contacts):
    with open("contacts.csv",'w',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(["Name","Phone","Email","Group"])

        for name,info in contacts.items():
            writer.writerow([name,info['Phone'],info['Email'],info['group']])

    print("Exported to contact.csv")



# ================= MENU ================= #

def menu():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All")
        print("6. Export CSV")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contacts(contacts)
            save_contacts(contacts)
        elif choice == '4':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            display_allcontacts(contacts)
        elif choice == '6':
            export_csv(contacts)
        elif choice == '7':
            save_contacts(contacts)
            print(" Saved. Exiting...")
            break
        else:
            print("Invalid choice!")

# ================= MAIN ================= 

if __name__ == "__main__":
    menu()