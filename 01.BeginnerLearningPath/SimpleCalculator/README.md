# Simple Calculator

A beginner-friendly Python command-line application that performs basic arithmetic operations including addition, subtraction, multiplication, and division.

## Features

- Perform basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with error handling for division by zero)
- User-friendly menu interface
- Input validation for numeric values
- Error handling for invalid inputs and division by zero
- Clean, readable output format
- Continuous operation until user chooses to exit

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository:
   ```
   git clone https://github.com/yourusername/simple-calculator.git
   cd simple-calculator
   ```
3. No additional dependencies are required.

## Usage

Run the program from the command line:

```
python calculator.py
```

Follow the on-screen menu prompts:
1. Select an operation (1-4) or exit (5)
2. Enter two numbers for the calculation
3. View the result
4. Choose to perform another calculation or exit

## Example

```
Simple Calculator
======================
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
======================
Enter your choice (1-5): 1
Enter first number: 10
Enter second number: 5
Result: 10 + 5 = 15

Would you like to perform another operation? (y/n): y

Simple Calculator
======================
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
======================
Enter your choice (1-5): 4
Enter first number: 20
Enter second number: 0
Error: Cannot divide by zero

Would you like to perform another operation? (y/n): y

Simple Calculator
======================
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
======================
Enter your choice (1-5): 3
Enter first number: 7
Enter second number: 8
Result: 7 * 8 = 56

Would you like to perform another operation? (y/n): n
Thank you for using the Simple Calculator. Goodbye!
```

## Project Structure

- `calculator.py`: Main program file containing all the calculator functionality

## Educational Value

This project demonstrates:
- Basic Python syntax and concepts
- Function definitions and usage
- User input handling and validation
- Error handling with try-except blocks
- Control flow using if/elif/else statements
- Basic arithmetic operations
- Command-line user interface design
- Loop structures for program flow control

## Future Enhancements

Potential improvements for future versions:
- Add more complex operations (square root, exponentiation, modulo)
- Implement memory functions (store and recall values)
- Allow for multi-step calculations
- Add a history feature to review previous calculations
- Create a simple graphical user interface (GUI)
- Support for scientific notation and large numbers
- Implement unit conversion capabilities
- Add a help command to explain operations