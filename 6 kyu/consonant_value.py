"""
https://www.codewars.com/kata/59c633e7dcc4053512000073/train/python
"""

def solve(s: str) -> int:
    if not s:
        return 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    new_s = s
    for ch in new_s:
        if ch in vowels:
            new_s = new_s.replace(ch, "_")
    while "__" in s:
        s = s.replace("__", "_")
    max_value = 0
    for word in new_s.split("_"):
        sum_value = 0
        for ch in word:
            sum_value += alphabet.index(ch) + 1
        if sum_value > max_value:
            max_value = sum_value
    return max_value

s = "strength"
print(solve(s))