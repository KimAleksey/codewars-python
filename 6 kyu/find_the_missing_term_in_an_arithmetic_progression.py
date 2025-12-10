"""
https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python

"""

def find_missing(sequence: list) -> int:
    prog_sum = ((len(sequence) + 1)/2)*(sequence[0]+sequence[-1])
    seq_sum = sum(sequence)
    res = int(prog_sum-seq_sum)
    return res


print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))