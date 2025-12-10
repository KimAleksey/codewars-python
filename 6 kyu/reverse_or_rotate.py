"""
https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python
"""

def rev_rot(strng: str, sz: int) -> str:
    if strng == "" or sz <= 0 or len(strng) < sz:
        return ""
    chunks = len(strng) // sz
    res = ""
    for i in range(chunks):
        if sum(map(int, strng[i*sz:i*sz+sz])) % 2 == 0:
            res += strng[i*sz:i*sz+sz][::-1]
        else:
            res += strng[i*sz+1:i*sz+sz] + strng[i*sz:i*sz+sz][0]
    return res


print(rev_rot("123456987654", 6))