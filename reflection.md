# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  When I first ran the game it looked like a normal guessing game but it didn't work properly. The hints were inconsistent and sometimes told me to go in the wrong direction even when I knew the correct answer. It also felt like the secret number was changing every time I clicked submit which made the game confusing and hard to win. Another issue was that the New Game button did not properly reset the game based on the selected difficulty. Overall the game was unplayable.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used ChatGPT as my main AI tool to help debug and understand the issues in the code. One correct suggestion it gave was to store the secret number in `st.session_state` and ensure it is consistently treated as an integer. This helped fix the issue where the game seemed to change the number or behave inconsistently. I verified this by running the app multiple times and confirming the number stayed the same across button clicks.

One misleading suggestion was when the AI initially used a `try/except` block in `check_guess` to handle type errors instead of fixing the root cause. This approach hid the real problem instead of solving it. I verified it was incorrect by removing the try/except and seeing that the real issue was caused by mixing string and integer types. This showed me that AI suggestions need to be carefully reviewed and not blindly trusted.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I verified bugs were fixed by manually testing the app and using pytest. For example, I tested that a guess of 60 against a secret of 50 correctly returns "Too High". I also added pytest tests to check different cases and edge cases. Seeing all tests pass gave me confidence that the logic was working correctly. AI helped by suggesting simple test cases that matched the expected behavior.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I learned that Streamlit reruns the entire script every time a user interacts with the app, such as clicking a button. This means that normal variables get reset unless they are stored in `st.session_state`. To maintain values like the secret number or score, they must be saved in session state. I would explain it like this: Streamlit is constantly restarting your program, so you need a special place (`session_state`) to remember things between runs.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is separating logic from UI code so that I can test functions independently using tools like pytest. This made debugging much easier and more structured. Next time I work with AI, I will be more critical of its suggestions and verify each change instead of assuming it is correct. This project showed me that AI-generated code is a good starting point, but it often contains bugs and needs careful review and testing before it can be trusted.
