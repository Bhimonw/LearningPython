# Currency Converter

A beginner-friendly Python command-line application that converts values between different currencies using predefined exchange rates.

## Features

- Convert between multiple currencies:
  - USD to EUR (US Dollar to Euro)
  - EUR to USD (Euro to US Dollar)
  - USD to GBP (US Dollar to British Pound)
  - GBP to USD (British Pound to US Dollar)
  - USD to IDR (US Dollar to Indonesian Rupiah)
  - IDR to USD (Indonesian Rupiah to US Dollar)
- User-friendly menu interface
- Input validation for numeric values
- Error handling for invalid inputs
- Clean, readable output format with proper currency symbols
- Continuous operation until user chooses to exit

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository:
   ```
   git clone https://github.com/Bhimonw/CurrencyConverter.git
   cd CurrencyConverter
   ```
3. No additional dependencies are required.

## Usage

Run the program from the command line:

```
python CurrencyConverter.py
```

Follow the on-screen menu prompts:
1. Select a conversion type (1-6) or exit (7)
2. Enter the amount you want to convert
3. View the result
4. Choose to perform another conversion or exit

## Example

```
Currency Converter
======================
1. USD to EUR
2. EUR to USD
3. USD to GBP
4. GBP to USD
5. USD to IDR
6. IDR to USD
7. Exit
======================
Enter your choice (1-7): 1
Enter amount in USD: 100
Converted amount: 100.00 USD = 85.00 EUR

Would you like to perform another conversion? (y/n): y

Currency Converter
======================
1. USD to EUR
2. EUR to USD
3. USD to GBP
4. GBP to USD
5. USD to IDR
6. IDR to USD
7. Exit
======================
Enter your choice (1-7): 5
Enter amount in USD: 10
Converted amount: 10.00 USD = 156500.00 IDR

Would you like to perform another conversion? (y/n): y

Currency Converter
======================
1. USD to EUR
2. EUR to USD
3. USD to GBP
4. GBP to USD
5. USD to IDR
6. IDR to USD
7. Exit
======================
Enter your choice (1-7): 6
Enter amount in IDR: 100000
Converted amount: 100000.00 IDR = 6.40 USD

Would you like to perform another conversion? (y/n): n
Thank you for using the Currency Converter. Goodbye!
```

## Conversion Rates

The program uses the following fixed conversion rates (for demonstration purposes):

- USD to EUR: 0.85 (1 USD = 0.85 EUR)
- EUR to USD: 1.18 (1 EUR = 1.18 USD)
- USD to GBP: 0.74 (1 USD = 0.74 GBP)
- GBP to USD: 1.35 (1 GBP = 1.35 USD)
- USD to IDR: 15650.00 (1 USD = 15,650 IDR)
- IDR to USD: 0.000064 (1 IDR = 0.000064 USD)

Note: In a real-world application, these rates would typically be fetched from an API to get current exchange rates.

## Project Structure

- `currency_converter.py`: Main program file containing all the converter functionality

## Educational Value

This project demonstrates:
- Basic Python syntax and concepts
- Function definitions and usage
- User input handling and validation
- Error handling with try-except blocks
- Control flow using if/elif/else statements
- Floating-point arithmetic and formatting
- Command-line user interface design
- Loop structures for program flow control

## Future Enhancements

Potential improvements for future versions:
- Add more currencies (JPY, CAD, AUD, etc.)
- Implement API integration to fetch real-time exchange rates
- Allow conversion between any two currencies (not just to/from USD)
- Add a feature to display historical exchange rate data
- Create a graphical user interface (GUI)
- Implement a command to show all available currencies
- Add a feature to save favorite or frequently used conversions
- Include a "reverse conversion" quick option
- Implement localization for currency formats (commas vs. periods, etc.)