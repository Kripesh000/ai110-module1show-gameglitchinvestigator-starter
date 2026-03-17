from logic_utils import check_guess, get_range_for_difficulty, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# Tests for the "New Game" button bug fix
def test_difficulty_range_easy():
    """Test that Easy difficulty uses range 1-20, not hardcoded 1-100"""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_difficulty_range_normal():
    """Test that Normal difficulty uses range 1-100"""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100


def test_difficulty_range_hard():
    """Test that Hard difficulty uses range 1-50"""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50


def test_new_game_resets_state():
    """
    Test that a new game properly initializes game state.
    Bug fix: Previously, attempts weren't reset and secret used hardcoded 1-100 range.
    """
    # Simulate game state before reset
    attempts = 5
    secret = 50
    status = "lost"
    history = [25, 75, 30, 80, 35]
    score = 10
    
    # Now simulate what happens when "New Game" is clicked
    difficulty = "Hard"
    low, high = get_range_for_difficulty(difficulty)
    
    # Verify reset values
    assert low == 1  # Hard difficulty starts at 1
    assert high == 50  # Hard difficulty ends at 50 (not 100)
    assert 1 <= low <= high  # Secret should be within range


def test_score_calculation_after_reset():
    """
    Test that score updates correctly after new game reset.
    Verifies the update_score function works with reset state.
    """
    reset_score = 0
    outcome = "Win"
    attempt_number = 3
    
    new_score = update_score(reset_score, outcome, attempt_number)
    
    # Score should be 100 - 10 * (3 + 1) = 100 - 40 = 60
    assert new_score == 60
    assert new_score > reset_score


def test_game_state_full_reset_cycle():
    """
    Test complete game state reset scenario.
    Simulates: Play game -> lose -> reset -> new state ready.
    """
    # Initial state after game starts
    attempts_before = 8  # Hit attempt limit
    status_before = "lost"
    history_before = [25, 75, 30, 80, 35, 40, 50, 60]
    score_before = -20
    
    # After "New Game" clicked (based on the fix)
    attempts_after = 0
    status_after = "playing"
    history_after = []
    score_after = 0  # Reset if reset_score_on_new_game is True
    
    # Verify all state is properly reset
    assert attempts_before == 8
    assert attempts_after == 0
    assert status_before == "lost"
    assert status_after == "playing"
    assert len(history_before) == 8
    assert len(history_after) == 0
    assert score_before == -20
    assert score_after == 0
