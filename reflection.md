# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What I expected: Clicking the "New Game" button should fully reset the game pick a new number, clear previous guesses, and let me start playing again immediately.
- What actually happened: Clicking "New Game" opened a new game screen but the game didn't actually continue or function. I had to manually reload the entire page in my browser to be able to play again.

- What I expected: When my guess was too high, the app should say "Go lower." When my guess was too low, the app should say "Go higher."
- What actually happened: The hints were reversed. The app said "Go higher" when my guess was too high and "Go lower" when my guess was too low, sending me in the wrong direction every time.

- What I expected: Each difficulty level should set a specific number range. For example, Easy might be 1–50, Medium might be 1–100, and Hard might be 1–200. The secret number should fall within that range.
- What actually happened: No matter which difficulty I selected (Easy, Medium, or Hard), the app just picked a random number without following any specific range. The difficulty setting had no real effect on gameplay.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
