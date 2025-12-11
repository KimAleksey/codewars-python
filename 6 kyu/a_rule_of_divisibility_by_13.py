"""
https://www.codewars.com/kata/564057bc348c7200bd0000ff/train/python
"""

def thirt(n):
    modes = [1, 10, 9, 12, 3, 4]
    new_n = list(map(int, str(n)))

    while True:
        buff = []
        for i in range(len(new_n)):
            buff.append(modes[i%6])
        s = 0
        for a, b in zip(buff, new_n[::-1]):
            s += a * b
        if new_n == list(map(int, str(s))):
            break
        new_n = list(map(int, str(s)))

    res = int(''.join(map(str, new_n)))
    return res

print(thirt(987654321))