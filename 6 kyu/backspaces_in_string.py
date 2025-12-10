"""
https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python
"""

def clean_string(s: str) -> str:
    if not s:
        return ""
    res = ""
    hash_cnt = 0
    for ch in s[::-1]:
        if ch == "#":
            hash_cnt += 1
        else:
            if hash_cnt == 0:
                res += ch
            else:
                hash_cnt -= 1
    return res[::-1]


print(clean_string(")#####.,c"))