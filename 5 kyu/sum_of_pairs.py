"""
https://www.codewars.com/kata/54d81488b981293527000c8f/train/python

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * the correct answer is the pair whose second value has the smallest index
== [3, 7]

"""

def sum_pairs(ints: list[int], s: int) -> list[int] | None:
    seen = set()
    for i in ints:
        y = s - i
        if y in seen:
            return [y, i]
        seen.add(i)
    return None


print(sum_pairs([10, 5, 2, 3, 7, 5],10))