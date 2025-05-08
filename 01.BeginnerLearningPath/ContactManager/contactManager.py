import csv
import os

def ensure_directory_exists(directory_path):
    """
    Ensures the target directory exists. If it doesn't exist, the directory will be created.
    
    Args:
        directory_path (str): Directory path to check/create
        
    Returns:
        bool: True if successful, False if failed
    """
    if not directory_path:
        return True  # If path is empty, it means current directory
        
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            print(f"Directory {directory_path} successfully created.")
            return True
        except Exception as e:
            print(f"Error: Failed to create directory: {e}")
            return False
    
    return True

def is_file_exists(file_path):
    """
    Checks if the file already exists
    
    Args:
        file_path (str): File path to check
        
    Returns:
        bool: True if file exists, False if it doesn't
    """
    return os.path.isfile(file_path)

def get_absolute_path(file_path):
    """
    Gets the absolute path of a file
    
    Args:
        file_path (str): File path
        
    Returns:
        str: Absolute path of the file
    """
    return os.path.abspath(file_path)

def add_contact(file_path):
    """
    Function to add a new contact to the CSV file
    
    Args:
        file_path (str): CSV file path to store contacts
    """
    print("\n=== Add New Contact ===")
    
    # Get user input
    name = input("Enter name: ").strip()
    phone_number = input("Enter phone number: ").strip()
    
    # Simple input validation
    if not name or not phone_number:
        print("Error: Name and phone number cannot be empty.")
        return
    
    # Make sure directory exists
    directory = os.path.dirname(file_path)
    if not ensure_directory_exists(directory):
        return
    
    # Check if file already exists
    file_exists = is_file_exists(file_path)
    
    try:
        # Open file for writing
        with open(file_path, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            
            # If it's a new file, add header
            if not file_exists:
                writer.writerow(['Name', 'Phone Number'])
            
            # Add new contact data
            writer.writerow([name, phone_number])
        
        # Confirm success
        print(f"Success: Contact '{name}' has been added!")
        print(f"Info: Data saved at: {get_absolute_path(file_path)}")
    except PermissionError:
        print("Error: No permission to write to file. Make sure you have the correct access.")
    except IOError as e:
        print(f"Error: Cannot write to file: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred while saving: {e}")

def display_table_header(header):
    """
    Displays the table header with a neat format
    
    Args:
        header (list): List containing header column names
    """
    # Define column widths
    name_width = 25
    phone_width = 20
    
    # Display header
    print(f"┌{'─' * name_width}┬{'─' * phone_width}┐")
    print(f"│ {header[0]:<{name_width-2}} │ {header[1]:<{phone_width-2}} │")
    print(f"├{'─' * name_width}┼{'─' * phone_width}┤")

def display_table_row(row, name_width=25, phone_width=20):
    """
    Displays a data row with a neat format
    
    Args:
        row (list): List containing data to be displayed
        name_width (int): Width of name column
        phone_width (int): Width of phone column
    """
    print(f"│ {row[0]:<{name_width-2}} │ {row[1]:<{phone_width-2}} │")

def display_table_footer(name_width=25, phone_width=20):
    """
    Displays the table footer
    
    Args:
        name_width (int): Width of name column
        phone_width (int): Width of phone column
    """
    print(f"└{'─' * name_width}┴{'─' * phone_width}┘")

def display_contacts(file_path):
    """
    Function to display all contacts from the CSV file in a neat table format
    
    Args:
        file_path (str): CSV file path containing contact data
    """
    print("\n=== Contact List ===")
    
    # Check if file exists
    if not is_file_exists(file_path):
        print("Info: Contact file doesn't exist yet. Please add a contact first.")
        return
    
    try:
        with open(file_path, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            
            # Read header
            header = next(reader, None)
            if not header:
                print("Error: Invalid file format or empty file.")
                return
                
            # Read all rows to count the number of contacts
            rows = list(reader)
            contact_count = len(rows)
            
            if contact_count == 0:
                print("Info: No contacts saved.")
                return
                
            # Display table header
            display_table_header(header)
            
            # Display each data row
            for row in rows:
                if len(row) >= 2:
                    display_table_row(row)
            
            # Display table footer
            display_table_footer()
            
            # Display contact count
            print(f"\nTotal: {contact_count} contacts.")
            
    except PermissionError:
        print("Error: No permission to read file.")
    except IOError as e:
        print(f"Error: Cannot read file: {e}")
    except Exception as e:
        print(f"Error: An error occurred while reading file: {e}")

def display_menu():
    """
    Displays the application menu
    
    Returns:
        str: Menu choice from user
    """
    print("\nSelect Menu:")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Exit")
    
    return input("\nEnter your choice (1/2/3): ").strip()

def main():
    """
    Main function to run the program
    """
    # Constants for file path
    FOLDER_PATH = "./csv/"
    FILE_NAME = "contacts.csv"
    file_path = os.path.join(FOLDER_PATH, FILE_NAME)
    
    # Application header
    print("╔════════════════════════════════╗")
    print("║     CONTACT MANAGEMENT APP     ║")
    print("╚════════════════════════════════╝")
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            add_contact(file_path)
        elif choice == '2':
            display_contacts(file_path)
        elif choice == '3':
            print("\nThank you for using this application!")
            break
        else:
            print("Error: Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()