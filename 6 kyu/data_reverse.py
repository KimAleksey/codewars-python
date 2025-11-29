"""
https://www.codewars.com/kata/569d488d61b812a0f7000015/train/python
"""

def data_reverse(data: list) -> list:
    buff = []
    for i in range(0, len(data), 8):
        buff.append(data[i:i+8])
    buff = buff[::-1]
    res = []
    for lst in buff:
        res.extend(lst)
    return res