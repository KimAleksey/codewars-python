"""
https://www.codewars.com/kata/51edd51599a189fe7f000015/train/python
"""

def solution(array_a, array_b):
    array = [(values[0]-values[1])**2 for values in zip(array_a, array_b)]
    return sum(array)/len(array)


print(solution([1, 2, 3], [4, 5, 6]))