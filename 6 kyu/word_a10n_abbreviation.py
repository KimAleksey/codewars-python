"""
https://www.codewars.com/kata/5375f921003bf62192000746/train/python

abbreviate("accessibility"), "a11y"
"""

def abbreviate(s: str) -> str:
    result = []
    word = ""
    for idx, char in enumerate(s):
        if char.isalpha():
            word += char
        else:
            if len(word) > 3:
                result.append(word[0] + str(len(word)-2) + word[-1])
            else:
                result.append(word)
            result.append(char)
            word = ""
        if idx == len(s) - 1:
            if len(word) > 3:
                result.append(word[0] + str(len(word)-2) + word[-1])
    return ''.join(result)



print(abbreviate("elephant-rides are really fun!"))