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
    print("7. Exit")
    print("================================")

def main():
    """Main program function"""
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1-7): "))
            
            if choice == 7:
                print("Thank you for using the Temperature Converter. Goodbye!")
                break
                
            if choice < 1 or choice > 7:
                print("Error: Please enter a number between 1 and 7.")
                continue
                
            # Get temperature input based on conversion type
            if choice == 1:
                temperature = get_numeric_input("Enter temperature in Celsius: ")
                result = celsius_to_fahrenheit(temperature)
                print(f"{temperature}°C is equal to {result:.2f}°F")
                
            elif choice == 2:
                temperature = get_numeric_input("Enter temperature in Fahrenheit: ")
                result = fahrenheit_to_celsius(temperature)
                print(f"{temperature}°F is equal to {result:.2f}°C")
                
            elif choice == 3:
                temperature = get_numeric_input("Enter temperature in Celsius: ")
                result = celsius_to_kelvin(temperature)
                print(f"{temperature}°C is equal to {result:.2f}K")
                
            elif choice == 4:
                temperature = get_numeric_input("Enter temperature in Kelvin: ")
                if temperature < 0:
                    print("Error: Kelvin cannot be negative.")
                    continue
                result = kelvin_to_celsius(temperature)
                print(f"{temperature}K is equal to {result:.2f}°C")
                
            elif choice == 5:
                temperature = get_numeric_input("Enter temperature in Fahrenheit: ")
                result = fahrenheit_to_kelvin(temperature)
                print(f"{temperature}°F is equal to {result:.2f}K")
                
            elif choice == 6:
                temperature = get_numeric_input("Enter temperature in Kelvin: ")
                if temperature < 0:
                    print("Error: Kelvin cannot be negative.")
                    continue
                result = kelvin_to_fahrenheit(temperature)
                print(f"{temperature}K is equal to {result:.2f}°F")
                
            # Ask if the user wants to perform another conversion
            continue_choice = input("\nWould you like to perform another conversion? (y/n): ").lower()
            if continue_choice != 'y':
                print("Thank you for using the Temperature Converter. Goodbye!")
                break
                
        except ValueError:
            print("Error: Please enter a valid number.")

if __name__ == "__main__":
    print("Welcome to the Temperature Converter!")
    main()