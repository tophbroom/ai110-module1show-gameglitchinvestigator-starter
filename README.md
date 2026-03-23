# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
   The hint wasn't correct and inconsistent, and you can't start a new game with the new game button
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
   Each time a button is clicked, Streamlit reruns the entire script. To preserve values like the secret number, they must be stored in st.session_state.
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.

4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

The game is a number guessing game built using streamlit. The user can select a difficulty and guess a number then it can receive feedback indicating whether the guess was too high, too low, or correct

The bugs founds are:

1. **State Bug**
   - The app reruns each time the submit button is click, this makes the secret number refresh
   - Need to store the values in st.session_state

2. **Wrong Hint Logic**
   - The hints were incorrect, "Too High" is shown instead of too low, vice versa

3. **Mix of logic and string**
   - the game logic had check_guess return both the string to return and the whether the guess was right making the logic check harder

- I refactored the core logic into the logic_utils.py file
- I fixed check_guess to only return the correct outcomes
- I corrected the hint messages so they are correct
- I added a few more pytest tests

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here](screenshot.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
