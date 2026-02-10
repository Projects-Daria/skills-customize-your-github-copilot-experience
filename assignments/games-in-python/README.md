
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a Hangman game using Python to practice string manipulation, loops, conditionals, and random selection. Players will guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Set Up Game Logic and Word Selection

#### Description
Create the foundation for the Hangman game by setting up word selection and initializing game state.

#### Requirements
Completed program should:

- Define a list of words to randomly select from
- Use the `random` module to select a word for each game
- Store game state including the selected word, guessed letters, and remaining attempts
- Display the initial hidden word format (e.g., `_ _ _ _`)

### 🛠️ Implement Guess Handling and Progress Display

#### Description
Build the core gameplay loop that processes player guesses and updates the game display.

#### Requirements
Completed program should:

- Accept letter guesses from the user via `input()`
- Check if the guessed letter is in the word
- Update and display the current progress (revealing guessed letters, keeping unrevealed as underscores)
- Track incorrect guesses and decrement remaining attempts
- Prevent duplicate guesses from counting against the player

### 🛠️ Complete Game Flow with Win/Lose Conditions

#### Description
Finish the game by implementing win/lose detection and handling game completion.

#### Requirements
Completed program should:

- Detect when the player wins (all letters guessed)
- Detect when the player loses (no attempts remaining)
- Display appropriate win/lose messages
- Show the final word on game end
- Prompt the player to play again or exit
