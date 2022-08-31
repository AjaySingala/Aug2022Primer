# palindrome.py
def is_palindrome(msg):
    return msg.upper() == msg[::-1].upper()

print(is_palindrome("bob"))
print(is_palindrome("abab"))
