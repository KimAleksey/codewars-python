"""
https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python
"""

def highest_rank(arr):
    if not arr:
        return 0
    s = set(arr)
    max_s = (-1, -1)
    for i in s:
        max_buff = (i, arr.count(i))
        if max_buff[1] > max_s[1] or (i > max_s[0] and max_buff[1] == max_s[1]):
            max_s = (i, max_buff[1])
    return max_s[0]


print(highest_rank([40, 6, 23, 5, 29, 17, 30, 25, 4, 24, 28, 23, 31, 31, 23, 28, 24, 38]))