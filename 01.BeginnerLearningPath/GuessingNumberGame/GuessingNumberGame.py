import random
import sys

class NumberGuessingGame:
    def __init__(self):
        self.min_num = 1
        self.max_num = 100
        self.attempts = 0
        self.max_attempts = None
        self.number_to_guess = 0
        self.hints_enabled = False
        self.hint_threshold = 5
        
    def set_difficulty(self):
        """Set the game difficulty level"""
        print("\n=== Choose Difficulty Level ===")
        print("1. Easy (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard (1-200)")
        print("4. Custom")
        
        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                
                if choice == 1:
                    self.min_num, self.max_num = 1, 50
                    break
                elif choice == 2:
                    self.min_num, self.max_num = 1, 100
                    break
                elif choice == 3:
                    self.min_num, self.max_num = 1, 200
                    break
                elif choice == 4:
                    self.min_num = int(input("Enter minimum number: "))
                    self.max_num = int(input("Enter maximum number: "))
                    if self.min_num >= self.max_num:
                        print("Invalid range! Minimum must be less than maximum.")
                        continue
                    break
                else:
                    print("Invalid choice! Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    def configure_game(self):
        """Configure game settings"""
        print("\n=== Game Configuration ===")
        
        # Set guess limit
        while True:
            limit_option = input("Would you like to set a guess limit? (y/n): ").lower()
            if limit_option == 'y':
                try:
                    self.max_attempts = int(input("Enter the maximum number of attempts: "))
                    if self.max_attempts <= 0:
                        print("Please enter a positive number.")
                        continue
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
            elif limit_option == 'n':
                self.max_attempts = None
                break
            else:
                print("Please enter 'y' or 'n'.")
        
        # Enable hints
        while True:
            hint_option = input("Would you like to enable hints after several wrong guesses? (y/n): ").lower()
            if hint_option == 'y':
                self.hints_enabled = True
                break
            elif hint_option == 'n':
                self.hints_enabled = False
                break
            else:
                print("Please enter 'y' or 'n'.")
    
    def get_valid_guess(self):
        """Get a valid numeric guess from the user"""
        while True:
            try:
                guess = int(input(f"Enter your guess ({self.min_num}-{self.max_num}): "))
                if self.min_num <= guess <= self.max_num:
                    return guess
                else:
                    print(f"Please enter a number between {self.min_num} and {self.max_num}.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    def provide_hint(self):
        """Provide a hint about the number"""
        if self.number_to_guess % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")
        
        # Additional hints based on number of attempts
        if self.attempts >= self.hint_threshold + 3:
            if self.number_to_guess % 5 == 0:
                print("Hint: The number is divisible by 5.")
            else:
                print("Hint: The number is not divisible by 5.")
    
    def play_game(self):
        """Main game logic"""
        # Set difficulty and configuration
        self.set_difficulty()
        self.configure_game()
        
        # Generate random number
        self.number_to_guess = random.randint(self.min_num, self.max_num)
        self.attempts = 0
        
        print(f"\n=== Let's Play! ===")
        print(f"I'm thinking of a number between {self.min_num} and {self.max_num}.")
        if self.max_attempts:
            print(f"You have {self.max_attempts} attempts to guess it.")
        
        # Main game loop
        while True:
            # Check if max attempts reached
            if self.max_attempts and self.attempts >= self.max_attempts:
                print(f"\nGame Over! You've used all {self.max_attempts} attempts.")
                print(f"The number was: {self.number_to_guess}")
                break
            
            self.attempts += 1
            guess = self.get_valid_guess()
            
            # Check the guess
            if guess == self.number_to_guess:
                print(f"\n🎉 Congratulations! You guessed the number in {self.attempts} attempt(s)!")
                break
            elif guess < self.number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
            
            # Provide hints if enabled and threshold reached
            if self.hints_enabled and self.attempts >= self.hint_threshold:
                self.provide_hint()
            
            # Show remaining attempts if limit is set
            if self.max_attempts:
                remaining = self.max_attempts - self.attempts
                if remaining > 0:
                    print(f"Attempts remaining: {remaining}")
    
    def play_again(self):
        """Ask if the player wants to play again"""
        while True:
            choice = input("\nWould you like to play again? (y/n): ").lower()
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            else:
                print("Please enter 'y' or 'n'.")

def main():
    """Main function to run the game"""
    print("Welcome to the Number Guessing Game!")
    print("====================================")
    
    game = NumberGuessingGame()
    
    while True:
        game.play_game()
        
        if not game.play_again():
            print("\nThank you for playing! Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()