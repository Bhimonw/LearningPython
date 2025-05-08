# Contact Management Application

## Description

The Contact Management Application is a Python program that allows users to add, display, and save contact information in a CSV file format. This program features a simple, text-based interface and ensures that users can easily input contact information such as names and phone numbers, as well as view a list of saved contacts.

## Features

* **Add New Contact:** Users can input a name and phone number, which will be saved in a CSV file.
* **Display Contacts:** The list of stored contacts will be displayed in a neat table format.
* **Automatic Directory Creation:** If the directory to store the CSV file doesn't exist, the program will create it automatically.
* **Informative Error Handling:** The application handles various errors such as permission issues, missing files, or input errors with clear messages.

## Implementations Used

### 1. **`os` Module**

The **`os`** module is used to interact with the operating system, allowing you to manage files and directories.

* **`os.path.exists()`**: Checks if a specified directory exists. Used to check if the directory where the CSV file should be stored already exists.
* **`os.makedirs()`**: Creates a new directory if it doesn't exist. Ensures the directory structure is in place before writing the CSV file.
* **`os.path.isdir()` and `os.path.isfile()`**: Used to check if a given path is a directory or file, respectively.

### 2. **`csv` Module**

The **`csv`** module is used for reading from and writing to CSV files, which is the format used to store contact information.

* **`csv.writer()`**: Writes data to a CSV file. This is used for adding new contacts (name and phone number) to the CSV file.
* **`csv.reader()`**: Reads data from the CSV file, allowing the program to display stored contacts in a readable format.

### 3. **File Operations**

* **Directory and File Handling:** Before writing to the CSV file, the program ensures that the directory exists and handles possible errors such as permission issues or file not found errors.
* **Directory Creation:** The program checks if the directory exists using `os.path.exists()` and creates it with `os.makedirs()` if it doesn't.
* **Error Handling:** The program handles file access errors such as **PermissionError** and **IOError** when reading or writing the CSV file.

### 4. **String Input and Validation**

* **Input Handling:** The program prompts the user for input (name and phone number) and performs basic validation to ensure that these fields are not left empty.
* **Input Validation:** If the user leaves either field empty, the program displays an error message and doesn't allow an empty contact to be added.

### 5. **Table Display Formatting**

* **Formatting Table Output:** The program displays contact information in a structured, tabular format.
* **`display_table_header()`**: Displays the table header (columns: Name, Phone Number).
* **`display_table_row()`**: Displays each row of contact data in a neat table format.
* **`display_table_footer()`**: Displays the footer of the table.

### 6. **Menu and User Interaction**

* The program presents a simple text-based menu to the user for interacting with the contact manager.
* **`tampilkan_menu()`**: Displays the menu options (add contact, display contacts, or exit).
* **Main Loop:** The program runs in a loop, continuously prompting the user for input until they choose to exit the application.

### 7. **Error Handling**

* The program handles multiple potential errors, including issues with file permissions, invalid file formats, and other unexpected exceptions.
* **Try-Except Blocks:** Used in the **`tambah_kontak()`** and **`tampilkan_kontak()`** functions to catch errors such as **PermissionError** and **IOError**.
* **Error Messages:** Informative error messages are displayed to help users understand issues, such as invalid file format or missing contacts.

### 8. **Absolute Path Retrieval**

* **`get_absolute_path()`**: This function returns the absolute path of the file being used (in this case, the contact file), which is useful for confirming the location where the contacts are stored.

---

## Installation

### **Prerequisites:**

* **Python 3.x** must be installed on your computer.
* No additional packages are required as the application uses standard Python modules like `csv` and `os`.

### **Installation Steps:**

* Copy the file `contactManager.py` to your preferred directory.
* Run the program with the following command in the terminal or command prompt:

  ```bash
  python contactManager.py
  ```

### **Directory Structure:**

* The application will automatically create the `./csv/` folder to store the `kontak.csv` file. Ensure you have permission to create folders and files in the specified directory.

## Usage

### 1. **Add a Contact:**

* Select option `1` to add a new contact.
* Enter the name and phone number when prompted. The data will be saved in the CSV file.

### 2. **Display Contacts:**

* Select option `2` to display all stored contacts.
* Contacts will be displayed in a table format with names and phone numbers.

### 3. **Exit:**

* Select option `3` to exit the application.

## Example Output

### Adding a Contact:

```bash
=== Add New Contact ===
Enter name: Rahmalia
Enter phone number: 081234567890
Success: Contact 'Rahmalia' has been added!
Info: Data saved to: /path/to/csv/kontak.csv
```

### Displaying Contacts:

```bash
=== Contact List ===
┌─────────────────────────┬────────────────────┐
│ Name                    │ Phone Number       │
├─────────────────────────┼────────────────────┤
│ Rahmalia                │ 081234567890       │
└─────────────────────────┴────────────────────┘
Total: 1 contact.
```

## Main Functions

1. **`add_contact(file_path)`**: Adds a new contact to the CSV file.
2. **`display_contact(file_path)`**: Displays all contacts in the CSV file in a table format.
3. **`create_directory(directory_path)`**: Ensures the directory for the CSV file exists; if not, it will be created.
4. **`write_contact_to_csv(file_path, name, phone_number, file_exists)`**: Writes a new contact to the CSV file, with handling for the header in case of a new file.
5. **`show_menu()`**: Displays the main menu of the application to choose an action (add, display, or exit).

## Error Handling

The application handles several types of errors, such as:

* **PermissionError:** If the application does not have permission to read/write the file.
* **IOError:** If there is an issue reading or writing the file.
* **Other Exceptions:** If any unforeseen errors occur during execution.

## Future Developments

* **User Authentication:** Adding authentication features to ensure only authorized users can access the application.
* **Import and Export:** Adding features to import or export contact data to/from other file formats (e.g., Excel or JSON).
* **Graphical User Interface (GUI):** Developing a GUI for this application using **Tkinter** or other frameworks.

---