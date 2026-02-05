```markdown
# 📘 Assignment: Hangman Game Challenge

**Difficulty:** Beginner  
**Estimated time:** 60–90 minutes

## 🎯 Objective

Build the classic word-guessing Hangman game using Python strings, loops, conditionals, and user input. Players will guess letters to reveal a hidden word before running out of attempts.

## 📂 Files
- `starter-code.py` — starter code with game skeleton and helper functions
- `solution.py` — (optional) reference implementation

## 🔧 Prerequisites
- Python 3.x
- Basic familiarity with strings, loops, conditionals, and the `random` module

## 📝 Tasks

### 🛠️ Build the Core Game Logic

#### Description
Create the main Hangman game structure that manages word selection, letter guessing, progress display, and win/lose conditions.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept letter guesses from the player
- Display current progress using underscores (e.g., `_ _ _ _`)
- Track incorrect guesses and remaining attempts
- Display win/lose messages
- Allow replaying the game

## 💡 Hints
- Use `random.choice()` to select a word from your list
- Store guessed letters in a set for fast lookup
- Create a helper function to display the current word state
- Consider using a loop to keep the game running until win/lose conditions are met

## ✅ How to run
From the repository root, run:

```bash
python3 assignments/games-in-python/starter-code.py
```

## 📤 Submission
- Save your completed solution as `solution.py` and submit via a pull request or ZIP upload.

```
