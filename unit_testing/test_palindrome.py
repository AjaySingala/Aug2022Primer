# test-palindrome.py
import pytest
from palindrome import is_palindrome

def test_is_palindrome_empty_string():
    assert is_palindrome("")

def test_is_palindrome_single_character():
    assert is_palindrome("a")

def test_is_palindrome_mixed_casing():
    assert is_palindrome("Bob")

def test_is_palindrome_lowercase():
    assert is_palindrome("racecar")

def test_is_palindrome_with_spaces():
    assert is_palindrome("Never odd or even") == False

def test_is_palindrome_with_punctuation():
    assert is_palindrome("Do geese see God?") == False

def test_is_palindrome_not_palindrome():
    assert not is_palindrome("abc")

def test_is_palindrome_not_quite():
    assert not is_palindrome("abab")

# @pytest.mark.parametrize("palindrome", [
#     "",
#     "a",
#     "Bob",
#     "racecar"
# ])
# def test_is_palindrome(palindrome):
#     assert is_palindrome(palindrome)

# @pytest.mark.parametrize("non_palindrome", [
#     "Never odd or even",
#     "Do geese see God?",
#     "abc",
#     "abab",
# ])
# def test_is_palindrome_not_palindrome(non_palindrome):
#     assert not is_palindrome(non_palindrome)
