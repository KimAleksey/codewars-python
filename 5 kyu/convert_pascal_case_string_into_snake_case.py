"""
https://www.codewars.com/kata/529b418d533b76924600085d/train/python
"""

def to_underscore(strng: str) -> str:
    if not strng:
        return ""
    if isinstance(strng, int):
        return str(strng)
    words = []
    idx_start = 0
    for idx, char in enumerate(strng):
        if idx == len(strng) - 1:
            words.append(strng[idx_start:idx+1].lower())
        if char.isupper() and strng[idx_start:idx] != "":
            words.append(strng[idx_start:idx].lower())
            idx_start = idx
    return "_".join(words)
