def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100

def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


# FIXME: Logic breaks here: The original hints were reversed it said "Go HIGHER" when the guess
# was too high and "Go LOWER" when the guess was too low, sending the player in
# the wrong direction. Also removed the unnecessary try/except TypeError block
# that converted guess to a string, which caused unreliable comparisons.

# BEFORE (buggy):
# if guess > secret:
#     return "Too High", "📈 Go HIGHER!"
# else:
#     return "Too Low", "📉 Go LOWER!"

def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!" 
    if guess > secret:
        return "Too High", "📈 Go Lower!"
    return "Too Low", "📉 Go Higher!"

def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points
## Fixed: removed inconsistent even/odd scoring on "Too High" — now both wrong guess types lose 5 points equally
    return current_score - 5    
   
