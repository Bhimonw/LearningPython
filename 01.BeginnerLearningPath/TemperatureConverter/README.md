# Temperature Converter

A simple Python command-line application that converts temperatures between Celsius, Fahrenheit, and Kelvin.

## Features

- Convert between multiple temperature units:
  - Celsius to Fahrenheit/Kelvin/Rankine
  - Fahrenheit to Celsius/Kelvin/Rankine
  - Kelvin to Celsius/Fahrenheit/Rankine
  - Rankine to Celsius/Fahrenheit/Kelvin
- User-friendly menu interface
- Robust input validation and error handling
- Physical constraint checks (e.g., Kelvin/Rankine cannot be negative)
- Consistently formatted output with units and configurable precision
- Modular code design for easy maintenance and extension

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
python temperature_converter.py
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
7. Celsius to Rankine
8. Rankine to Celsius
9. Fahrenheit to Rankine
10. Rankine to Fahrenheit
11. Kelvin to Rankine
12. Rankine to Kelvin
13. Exit
================================
Enter your choice (1-13): 1
Enter temperature in Celsius: 25
25°C is equal to 77.00°F

Would you like to perform another conversion? (y/n): y

===== Temperature Converter =====
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
7. Celsius to Rankine
8. Rankine to Celsius
9. Fahrenheit to Rankine
10. Rankine to Fahrenheit
11. Kelvin to Rankine
12. Rankine to Kelvin
13. Exit
================================
Enter your choice (1-13): abc
Error: Please enter a valid number between 1 and 13.
Enter your choice (1-13): 7
Enter temperature in Celsius: 30
30°C is equal to 545.67°R

Would you like to perform another conversion? (y/n): n
Thank you for using the Temperature Converter. Goodbye!
```

## Temperature Conversion Formulas

The program uses the following formulas for conversions:

### Basic Conversions:
- Celsius to Fahrenheit: `(Celsius * 9/5) + 32`
- Fahrenheit to Celsius: `(Fahrenheit - 32) * 5/9`
- Celsius to Kelvin: `Celsius + 273.15`
- Kelvin to Celsius: `Kelvin - 273.15`

### Compound Conversions:
- Fahrenheit to Kelvin: First convert to Celsius, then to Kelvin
- Kelvin to Fahrenheit: First convert to Celsius, then to Fahrenheit

### Rankine Scale Conversions:
- Celsius to Rankine: `(Celsius + 273.15) * 9/5`
- Rankine to Celsius: `(Rankine * 5/9) - 273.15`
- Fahrenheit to Rankine: `Fahrenheit + 459.67`
- Rankine to Fahrenheit: `Rankine - 459.67`
- Kelvin to Rankine: `Kelvin * 9/5`
- Rankine to Kelvin: `Rankine * 5/9`

Note: Both Kelvin and Rankine are absolute temperature scales, meaning they cannot have negative values (absolute zero is the minimum possible temperature in the universe).

## Project Structure

Current structure:
- `temperature_converter.py`: Main program file containing all the code

For future development, consider refactoring into this structure:
- `temperature_converter/`
  - `__init__.py`: Package initialization
  - `conversions.py`: Temperature conversion functions
  - `ui.py`: User interface functions
  - `main.py`: Program entry point
  - `utils.py`: Utility functions for input validation, etc.

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
- Add a graphical user interface (GUI) using Tkinter, PyQt, or web interface
- Implement batch conversions from CSV or Excel files
- Add more temperature scales (Réaumur, Newton, Delisle, etc.)
- Include temperature conversion history with option to export
- Add temperature facts based on the input values (e.g., boiling/freezing points, weather references)
- Include scientific precision options for different use cases
- Implement unit testing for conversion formulas
- Add visualization of temperature scales with comparative chart
- Create a REST API for programmatic temperature conversions