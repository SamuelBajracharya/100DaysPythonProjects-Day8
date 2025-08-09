# 📒 Contact Dictionary (Python CLI)

A simple **menu-driven Contact Dictionary** program written in Python.  
This CLI (Command-Line Interface) tool allows you to **view, search, add, edit, and remove contacts** stored in memory.

---

## 🚀 Features
- **View all contacts** — Displays every contact with their email and phone.
- **Search a contact** — Find a contact by name.
- **Add a new contact** — Add name, email, and phone number.
- **Edit a contact** — Update details of an existing contact.
- **Remove a contact** — Delete a contact from the dictionary.
- **Exit the program** — Close the application.

---

## 🛠 Requirements
- Python 3.x

No external libraries are needed — the program uses only Python's built-in functions.

---

## 📂 Project Structure
```
contact_dictionary/
│
├── main.py                # Main entry point (menu loop)
├── contact_dictionary.py   # Contains all contact operations
└── README.md               # Project documentation
```

---

## ▶️ How to Run

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/contact-dictionary.git
cd contact-dictionary
```

2. **Run the program**
```bash
python main.py
```

---

## 📋 Menu Options
When you run the program, you'll see:
```
Menu:
1. View all contacts.
2. Search a contact from the dictionary.
3. Add a new contact to the dictionary.
4. Edit a contact in the dictionary.
5. Remove a contact from the dictionary.
6. Exit the program
```
Type the corresponding number to choose an action.

---

## 💡 Example Run
```
Menu:
1. View all contacts.
2. Search a contact from the dictionary.
3. Add a new contact to the dictionary.
4. Edit a contact in the dictionary.
5. Remove a contact from the dictionary.
6. Exit the program
Please select an option from the menu above.
Enter your choice: 3
Enter name of contact: John Doe
Enter email of contact: john@example.com
Enter phone of contact: 1234567890
Contact added to the contact dictionary.
```

---

## ⚠ Limitations
- Contacts are **not saved** after exiting (stored in memory only).
- Names must be unique (adding an existing name will overwrite the old contact).

---

## 📌 Future Improvements
- Save contacts to a file (CSV/JSON) for persistence.
- Add email and phone validation.
- Allow multiple phone numbers/emails per contact.

---

## 📝 License
This project is licensed under the MIT License.
