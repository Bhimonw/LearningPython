# Contact Manager

A simple Python command-line application that allows you to store and manage contact information.

## Features

- Manage your contacts with ease:
  - Add new contacts with name and phone number
  - View all contacts in a formatted table
  - Automatic storage in CSV format
  - Clear error handling and validation
  - Directory auto-creation if needed

- User-friendly interface:
  - Menu-driven operation
  - Clearly formatted tables
  - Helpful status messages
  - Error notifications

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository:
   ```
   git clone https://github.com/yourusername/contact-manager.git
   cd contact-manager
   ```
3. No additional dependencies are required.

## Usage

Run the program from the command line:

```
python contact_manager.py
```

Follow the on-screen menu prompts:

1. Select an operation (1-3)
2. Add contacts or view existing ones
3. Exit when finished

## Example

```
╔════════════════════════════════╗
║     CONTACT MANAGEMENT APP     ║
╚════════════════════════════════╝

Select Menu:
1. Add Contact
2. Display Contacts
3. Exit

Enter your choice (1/2/3): 1

=== Add New Contact ===
Enter name: John Doe
Enter phone number: 555-123-4567
Success: Contact 'John Doe' has been added!
Info: Data saved at: C:\Users\username\contact-manager\csv\contacts.csv

Select Menu:
1. Add Contact
2. Display Contacts
3. Exit

Enter your choice (1/2/3): 2

=== Contact List ===
┌─────────────────────────┬────────────────────┐
│ Name                    │ Phone Number       │
├─────────────────────────┼────────────────────┤
│ John Doe                │ 555-123-4567       │
└─────────────────────────┴────────────────────┘

Total: 1 contacts.

Select Menu:
1. Add Contact
2. Display Contacts
3. Exit

Enter your choice (1/2/3): 3

Thank you for using this application!
```

## File Storage

The program stores all contacts in a CSV file:
- Location: `./csv/contacts.csv`
- Format: Standard CSV with headers
- Auto-created on first contact addition

## Project Structure

- `contact_manager.py`: Main program file containing all the code
- `csv/` directory: Created automatically to store the contact database

## Educational Value

This project demonstrates:
- File I/O operations in Python
- CSV data handling
- Function-based modular programming
- User input processing and validation
- Error handling with try-except blocks
- Pretty-printing tabular data
- Basic directory and file manipulation

## Future Enhancements

Potential improvements for future versions:
- Search functionality to find specific contacts
- Edit and delete operations for contacts
- Contact categorization or grouping
- Phone number format validation
- Import/export features with other formats
- Backup and restore functionality
- Contact sorting options
- Pagination for large contact lists
