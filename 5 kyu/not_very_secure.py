"""
https://www.codewars.com/kata/526dbd6c8c0eb53254000110/train/python
"""

def alphanumeric(password: str) -> bool:
    if not password.replace(' ', ''):
        return False
    return all([ch.isalnum() for ch in password])