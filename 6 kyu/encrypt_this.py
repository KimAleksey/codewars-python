"""
https://www.codewars.com/kata/5848565e273af816fb000449/train/python
"""

def encrypt_this(text):
    if not text:
        return ""
    res = []
    for word in text.split():
        if len(word) == 1:
            new_word = str(ord(word))
        elif len(word) == 2:
            new_word = str(ord(word[0])) + word[1]
        elif len(word) == 3:
            new_word = str(ord(word[0])) + word[1:][::-1]
        else:
            new_word = str(ord(word[0])) + word[-1] + word[2:len(word)-1] + word[1]
        res.append(new_word)
    return " ".join(res)


assert encrypt_this("hello world") == "104olle 119drlo"
assert encrypt_this("A wise old owl lived in an oak") == "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
assert encrypt_this("The more he saw the less he spoke") == "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"
assert encrypt_this("The less he spoke the more he heard") == "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"
assert encrypt_this("Why can we not all be like that wise old bird") == "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"
assert encrypt_this("Thank you Piotr for all your help") == "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"

print("yes")