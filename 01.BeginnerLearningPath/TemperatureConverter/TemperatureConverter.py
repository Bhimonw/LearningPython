def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    # First convert to Celsius, then to Kelvin
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    # First convert to Celsius, then to Fahrenheit
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

# Additional temperature conversion functions
def celsius_to_rankine(celsius):
    """Convert Celsius to Rankine"""
    return (celsius + 273.15) * 9/5

def rankine_to_celsius(rankine):
    """Convert Rankine to Celsius"""
    return (rankine * 5/9) - 273.15

def fahrenheit_to_rankine(fahrenheit):
    """Convert Fahrenheit to Rankine"""
    return fahrenheit + 459.67

def rankine_to_fahrenheit(rankine):
    """Convert Rankine to Fahrenheit"""
    return rankine - 459.67

def kelvin_to_rankine(kelvin):
    """Convert Kelvin to Rankine"""
    return kelvin * 9/5

def rankine_to_kelvin(rankine):
    """Convert Rankine to Kelvin"""
    return rankine * 5/9

def get_numeric_input(prompt):
    """Get a valid numeric input from the user"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

def display_menu():
    """Display the conversion menu options"""
    print("\n===== Temperature Converter =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Celsius to Rankine")
    print("8. Rankine to Celsius")
    print("9. Fahrenheit to Rankine")
    print("10. Rankine to Fahrenheit")
    print("11. Kelvin to Rankine")
    print("12. Rankine to Kelvin")
    print("13. Exit")
    print("================================")

def get_menu_choice(max_choice):
    """Get a valid menu choice from the user"""
    while True:
        try:
            choice_str = input(f"Enter your choice (1-{max_choice}): ")
            choice = int(choice_str)
            
            if choice < 1 or choice > max_choice:
                print(f"Error: Please enter a number between 1 and {max_choice}.")
                continue
                
            return choice
        except ValueError:
            print(f"Error: Please enter a valid number between 1 and {max_choice}.")

def check_kelvin_negative(temperature, unit="Kelvin"):
    """Check if a Kelvin or Rankine temperature is negative"""
    if temperature < 0:
        print(f"Error: {unit} cannot be negative (absolute zero is the minimum possible temperature).")
        return True
    return False

def format_result(input_value, input_unit, result, result_unit, precision=2):
    """Format the conversion result with appropriate units and precision"""
    return f"{input_value}{input_unit} is equal to {result:.{precision}f}{result_unit}"

def main():
    """Main program function"""
    while True:
        display_menu()
        
        # Get menu choice with improved error handling
        max_choice = 13  # Update this if adding more conversions
        choice = get_menu_choice(max_choice)
        
        if choice == max_choice:  # Exit option
            print("Thank you for using the Temperature Converter. Goodbye!")
            break
            
        # Get temperature input based on conversion type
        if choice == 1:
            temperature = get_numeric_input("Enter temperature in Celsius: ")
            result = celsius_to_fahrenheit(temperature)
            print(format_result(temperature, "°C", result, "°F"))
            
        elif choice == 2:
            temperature = get_numeric_input("Enter temperature in Fahrenheit: ")
            result = fahrenheit_to_celsius(temperature)
            print(format_result(temperature, "°F", result, "°C"))
            
        elif choice == 3:
            temperature = get_numeric_input("Enter temperature in Celsius: ")
            result = celsius_to_kelvin(temperature)
            print(format_result(temperature, "°C", result, "K"))
            
        elif choice == 4:
            temperature = get_numeric_input("Enter temperature in Kelvin: ")
            if check_kelvin_negative(temperature):
                continue
            result = kelvin_to_celsius(temperature)
            print(format_result(temperature, "K", result, "°C"))
            
        elif choice == 5:
            temperature = get_numeric_input("Enter temperature in Fahrenheit: ")
            result = fahrenheit_to_kelvin(temperature)
            print(format_result(temperature, "°F", result, "K"))
            
        elif choice == 6:
            temperature = get_numeric_input("Enter temperature in Kelvin: ")
            if check_kelvin_negative(temperature):
                continue
            result = kelvin_to_fahrenheit(temperature)
            print(format_result(temperature, "K", result, "°F"))
            
        elif choice == 7:
            temperature = get_numeric_input("Enter temperature in Celsius: ")
            result = celsius_to_rankine(temperature)
            print(format_result(temperature, "°C", result, "°R"))
            
        elif choice == 8:
            temperature = get_numeric_input("Enter temperature in Rankine: ")
            if check_kelvin_negative(temperature, "Rankine"):
                continue
            result = rankine_to_celsius(temperature)
            print(format_result(temperature, "°R", result, "°C"))
            
        elif choice == 9:
            temperature = get_numeric_input("Enter temperature in Fahrenheit: ")
            result = fahrenheit_to_rankine(temperature)
            print(format_result(temperature, "°F", result, "°R"))
            
        elif choice == 10:
            temperature = get_numeric_input("Enter temperature in Rankine: ")
            if check_kelvin_negative(temperature, "Rankine"):
                continue
            result = rankine_to_fahrenheit(temperature)
            print(format_result(temperature, "°R", result, "°F"))
            
        elif choice == 11:
            temperature = get_numeric_input("Enter temperature in Kelvin: ")
            if check_kelvin_negative(temperature):
                continue
            result = kelvin_to_rankine(temperature)
            print(format_result(temperature, "K", result, "°R"))
            
        elif choice == 12:
            temperature = get_numeric_input("Enter temperature in Rankine: ")
            if check_kelvin_negative(temperature, "Rankine"):
                continue
            result = rankine_to_kelvin(temperature)
            print(format_result(temperature, "°R", result, "K"))
            
        # Ask if the user wants to perform another conversion
        continue_choice = input("\nWould you like to perform another conversion? (y/n): ").lower()
        if continue_choice != 'y':
            print("Thank you for using the Temperature Converter. Goodbye!")
            break

if __name__ == "__main__":
    print("Welcome to the Temperature Converter!")
    main()