# Number Guessing Game

A fun and interactive Python game where players try to guess a randomly generated number. The game provides feedback on whether guesses are too high or too low, and includes various difficulty levels and optional features.

## Features

- **Multiple Difficulty Levels**:
  - Easy (1-50)
  - Medium (1-100)
  - Hard (1-200)
  - Custom range
- **Optional Guess Limit**: Set a maximum number of attempts
- **Hint System**: Get helpful hints after several wrong guesses
- **Input Validation**: Handles invalid inputs gracefully
- **Score Tracking**: Shows the number of attempts taken
- **Play Again Option**: Continue playing multiple rounds

## Installation

1. Ensure you have Python 3.x installed on your system
2. Clone or download this repository:
   ```bash
   git clone https://github.com/yourusername/number-guessing-game.git
   cd number-guessing-game
   ```
3. No additional dependencies required!

## How to Play

1. Run the game:
   ```bash
   python number_guessing_game.py
   ```

2. Choose your difficulty level
3. Configure game settings (guess limit and hints)
4. Start guessing the number!
5. Follow the feedback to narrow down your guesses
6. Try to guess the number in as few attempts as possible

## Example Gameplay

```
Welcome to the Number Guessing Game!
====================================

=== Choose Difficulty Level ===
1. Easy (1-50)
2. Medium (1-100)
3. Hard (1-200)
4. Custom
Enter your choice (1-4): 2

=== Game Configuration ===
Would you like to set a guess limit? (y/n): y
Enter the maximum number of attempts: 10
Would you like to enable hints after several wrong guesses? (y/n): y

=== Let's Play! ===
I'm thinking of a number between 1 and 100.
You have 10 attempts to guess it.
Enter your guess (1-100): 50
Too low! Try again.
Attempts remaining: 9
Enter your guess (1-100): 75
Too high! Try again.
Attempts remaining: 8
Enter your guess (1-100): 62
Too low! Try again.
Attempts remaining: 7
Enter your guess (1-100): 68
Too high! Try again.
Attempts remaining: 6
Enter your guess (1-100): 65
Too low! Try again.
Hint: The number is odd.
Attempts remaining: 5
Enter your guess (1-100): 67

🎉 Congratulations! You guessed the number in 6 attempt(s)!

Would you like to play again? (y/n): n

Thank you for playing! Goodbye!
```

## Code Structure

The game is built using object-oriented programming principles:

- `NumberGuessingGame` class: Contains all game logic and state
  - `set_difficulty()`: Handles difficulty selection
  - `configure_game()`: Sets up optional features
  - `get_valid_guess()`: Validates user input
  - `provide_hint()`: Generates hints based on game state
  - `play_game()`: Main game loop
  - `play_again()`: Handles replay logic

## Key Concepts Demonstrated

1. **Random Number Generation**: Using Python's `random` module
2. **Object-Oriented Programming**: Class-based structure
3. **Input Validation**: Try-except blocks for error handling
4. **Loops**: While loops for game flow
5. **Conditionals**: If-elif-else statements for game logic
6. **User Interaction**: Input/output operations

## Educational Value

This project is perfect for beginners to practice:
- Basic Python syntax and control structures
- Exception handling for robust user input
- Object-oriented programming concepts
- Game logic and state management
- Interactive program development

## Customization Options

You can easily modify the game by:
- Adjusting the default number ranges
- Adding more hint types (divisibility by other numbers, prime numbers, etc.)
- Implementing a scoring system based on attempts
- Adding difficulty-based scoring multipliers
- Creating a high score system

## Future Enhancements

Potential improvements for future versions:
- GUI interface using tkinter or pygame
- Multiplayer mode (competitive or cooperative)
- Different game modes (time-based, reverse guessing)
- Statistics tracking (average attempts, success rate)
- Sound effects and visual feedback
- Online leaderboard
- Machine learning opponent that learns from player patterns

## Contributing

Feel free to fork this project and submit pull requests with improvements!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by classic number guessing games
- Built as an educational project for Python beginners