"""
https://www.codewars.com/kata/53697be005f803751e0015aa/train/python
"""

def encode(st):
    t = str.maketrans("aeiou", "12345")
    res = st.translate(t)
    # vowels = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
    # res = ''.join(ch if ch not in vowels else vowels[ch] for ch in st)
    return res

def decode(st):
    t = str.maketrans("12345", "aeiou")
    res = st.translate(t)
    # vowels = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u"}
    # res = ''.join(ch if ch not in vowels else vowels[ch] for ch in st)
    return res

print(encode("hello"))
print(decode("h3 th2r2"))