def usd_to_eur(amount):
    """Convert USD to EUR"""
    # Using a fixed conversion rate for demonstration purposes
    rate = 0.85
    return amount * rate

def eur_to_usd(amount):
    """Convert EUR to USD"""
    # Using a fixed conversion rate for demonstration purposes
    rate = 1.18
    return amount * rate

def usd_to_gbp(amount):
    """Convert USD to GBP"""
    # Using a fixed conversion rate for demonstration purposes
    rate = 0.74
    return amount * rate

def gbp_to_usd(amount):
    """Convert GBP to USD"""
    # Using a fixed conversion rate for demonstration purposes
    rate = 1.35
    return amount * rate

def usd_to_idr(amount):
    """Convert USD to IDR (Indonesian Rupiah)"""
    # Using a fixed conversion rate for demonstration purposes
    rate = 15650.0
    return amount * rate

def idr_to_usd(amount):
    """Convert IDR (Indonesian Rupiah) to USD"""
    # Using a fixed conversion rate for demonstration purposes
    rate = 0.000064
    return amount * rate

def get_valid_number(prompt):
    """Function to get and validate numeric input from the user"""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
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
    """Function to display the currency converter menu"""
    print("\nCurrency Converter")
    print("======================")
    print("1. USD to EUR")
    print("2. EUR to USD")
    print("3. USD to GBP")
    print("4. GBP to USD")
    print("5. USD to IDR")
    print("6. IDR to USD")
    print("7. Exit")
    print("======================")

def main():
    """Main function to run the currency converter program"""
    while True:
        display_menu()
        
        # Get user's choice
        choice = get_valid_choice("Enter your choice (1-7): ", ["1", "2", "3", "4", "5", "6", "7"])
        
        # Exit if user chooses 7
        if choice == "7":
            print("Thank you for using the Currency Converter. Goodbye!")
            break
        
        # Determine the input currency and conversion function based on user's choice
        if choice == "1":
            input_currency = "USD"
            output_currency = "EUR"
            conversion_function = usd_to_eur
        elif choice == "2":
            input_currency = "EUR"
            output_currency = "USD"
            conversion_function = eur_to_usd
        elif choice == "3":
            input_currency = "USD"
            output_currency = "GBP"
            conversion_function = usd_to_gbp
        elif choice == "4":
            input_currency = "GBP"
            output_currency = "USD"
            conversion_function = gbp_to_usd
        elif choice == "5":
            input_currency = "USD"
            output_currency = "IDR"
            conversion_function = usd_to_idr
        elif choice == "6":
            input_currency = "IDR"
            output_currency = "USD"
            conversion_function = idr_to_usd
        
        # Get amount for conversion
        amount = get_valid_number(f"Enter amount in {input_currency}: ")
        
        # Perform the conversion
        converted_amount = conversion_function(amount)
        
        # Display the result (rounded to 2 decimal places for currency)
        print(f"Converted amount: {amount:.2f} {input_currency} = {converted_amount:.2f} {output_currency}")
        
        # Ask if the user wants to perform another conversion
        continue_choice = get_valid_choice("Would you like to perform another conversion? (y/n): ", ["y", "n"])
        if continue_choice.lower() == "n":
            print("Thank you for using the Currency Converter. Goodbye!")
            break

if __name__ == "__main__":
    main()