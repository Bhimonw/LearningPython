# Temperature Converter

A simple Python command-line application that converts temperatures between Celsius, Fahrenheit, and Kelvin.

## Features

- Convert between multiple temperature units:
  - Celsius to Fahrenheit
  - Fahrenheit to Celsius
  - Celsius to Kelvin
  - Kelvin to Celsius
  - Fahrenheit to Kelvin
  - Kelvin to Fahrenheit
- User-friendly menu interface
- Input validation and error handling
- Properly formatted output with units

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository:
   ```
   git clone https://github.com/yourusername/temperature-converter.git
   cd temperature-converter
   ```
3. No additional dependencies are required.

## Usage

Run the program from the command line:

```
python TemperatureConverter.py
```

Follow the on-screen menu prompts:
1. Select a conversion type (1-6) or exit (7)
2. Enter the temperature value to convert
3. View the result
4. Choose to perform another conversion or exit

## Example

```
Welcome to the Temperature Converter!

===== Temperature Converter =====
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
7. Exit
================================
Enter your choice (1-7): 1
Enter temperature in Celsius: 25
25.0°C is equal to 77.00°F

Would you like to perform another conversion? (y/n): y

===== Temperature Converter =====
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
7. Exit
================================
Enter your choice (1-7): 3
Enter temperature in Celsius: 30
30.0°C is equal to 303.15K

Would you like to perform another conversion? (y/n): n
Thank you for using the Temperature Converter. Goodbye!
```

## Temperature Conversion Formulas

The program uses the following formulas for conversions:

- Celsius to Fahrenheit: `(Celsius * 9/5) + 32`
- Fahrenheit to Celsius: `(Fahrenheit - 32) * 5/9`
- Celsius to Kelvin: `Celsius + 273.15`
- Kelvin to Celsius: `Kelvin - 273.15`
- Fahrenheit to Kelvin: First convert to Celsius, then to Kelvin
- Kelvin to Fahrenheit: First convert to Celsius, then to Fahrenheit

## Project Structure

- `TemperatureConverter.py`: Main program file containing all the code

## Educational Value

This project demonstrates:
- Basic Python syntax and concepts
- Functions and modular code organization
- User input handling and validation
- Error handling with try-except blocks
- Control flow (if/elif/else statements)
- Scientific calculations
- Command-line user interface design

## Future Enhancements

Potential improvements for future versions:
- Add a graphical user interface (GUI)
- Implement batch conversions from a file
- Add more temperature scales (Rankine, Réaumur, etc.)
- Include temperature conversion history
- Add temperature facts based on the input values