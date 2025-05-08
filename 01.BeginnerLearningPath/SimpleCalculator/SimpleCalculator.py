def add(num1, num2):
    """Function to add two numbers"""
    return num1 + num2

def subtract(num1, num2):
    """Function to subtract the second number from the first"""
    return num1 - num2

def multiply(num1, num2):
    """Function to multiply two numbers"""
    return num1 * num2

def divide(num1, num2):
    """Function to divide the first number by the second"""
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

def get_valid_number(prompt):
    """Function to get and validate numeric input from the user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_valid_choice(prompt, valid_choices):
    """Function to get and validate menu choice from the user"""
    while True:
        choice = input(prompt)
        if choice in valid_choices:
            return choice
        print(f"Invalid choice! Please enter one of the following: {', '.join(valid_choices)}")

def display_menu():
    """Function to display the calculator menu"""
    print("\nSimple Calculator")
    print("======================")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("======================")

def main():
    """Main function to run the calculator program"""
    while True:
        display_menu()
        
        # Get user's choice
        choice = get_valid_choice("Enter your choice (1-5): ", ["1", "2", "3", "4", "5"])
        
        # Exit if user chooses 5
        if choice == "5":
            print("Thank you for using the Simple Calculator. Goodbye!")
            break
        
        # Get numbers for calculation
        num1 = get_valid_number("Enter first number: ")
        num2 = get_valid_number("Enter second number: ")
        
        # Perform the calculation based on user's choice
        try:
            if choice == "1":
                result = add(num1, num2)
                operation = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                operation = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                operation = "*"
            elif choice == "4":
                result = divide(num1, num2)
                operation = "/"
            
            # Display the result
            print(f"Result: {num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        
        # Ask if the user wants to perform another calculation
        continue_choice = get_valid_choice("Would you like to perform another operation? (y/n): ", ["y", "n"])
        if continue_choice.lower() == "n":
            print("Thank you for using the Simple Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()