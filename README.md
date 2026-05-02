# Contact Management System

A Python-based contact management system built using dictionaries and functions.
Supports full CRUD operations, search, file persistence, and CSV export.

---

## How to Run

```bash
cd contact-management-system
python contact_manager.py
```

To run tests:
```bash
python test_contacts.py
```

---

## Features

- Add new contacts with validation
- Search contacts by name (partial match)
- Update existing contact details
- Delete contacts with confirmation
- View all contacts
- Export contacts to CSV
- Save and load data using JSON

---

## Project Structure

```
contact-management-system/
├── contact_manager.py
├── contacts_data.json
├── contacts.csv
├── test_contacts.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Data Structure

```python
contacts = {
    "Anand Yadav": {
        "Phone": "7778889991",
        "Email": "anand@gmail.com",
        "group": "Home",
        "address": "Bhubaneswar",
        "Created at": "2026-05-02T12:47:06",
        "Updated at": "2026-05-02T12:47:06"
    }
}
```

---

## Sample Output

```
===== CONTACT MANAGEMENT SYSTEM =====
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All
6. Export CSV
7. Exit
Enter choice: 1
----Add Contacts----
Enter The Name: Anand Yadav
Enter Phone Number: 7778889991
Enter your email: anand@gmail.com
Enter Your Address: Bhubaneswar
Enter your Group: Home
Contact added successfully.
```

---

## What I Learned

- Functions: writing reusable, organized code
- Dictionaries: storing and retrieving data with key-value pairs
- File Operations: saving and loading data using JSON
- Input Validation: phone and email validation using regex
- Error Handling: handling missing files, invalid inputs, duplicates

---

## Developer

**Anand Sagar Rout**  
Week 3 Project — Functions & Dictionaries  
Python Development Internship @ CrackOne Technologies