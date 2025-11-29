"""
https://www.codewars.com/kata/59df2f8f08c6cec835000012/train/python
"""

def meeting(s):
    names = [ name.upper().split(":") for name in s.split(";")]
    buff = sorted(names, key=lambda x: (x[1], x[0]))
    res = []
    for name in buff:
        res.append(f"({name[1]}, {name[0]})")
    return ''.join(res)


s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(meeting(s))