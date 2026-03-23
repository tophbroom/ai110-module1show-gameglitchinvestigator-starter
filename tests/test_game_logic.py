from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
    
def test_check_guess_returns_string():
    result = check_guess(60, 50)
    assert isinstance(result, str)
    
def test_guess_with_small_numbers():
    result = check_guess(1, 2)
    assert result == "Too Low"

def test_guess_with_large_numbers():
    result = check_guess(1000, 10)
    assert result == "Too High"
