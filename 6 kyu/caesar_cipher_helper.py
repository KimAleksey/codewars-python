"""
https://www.codewars.com/kata/526d42b6526963598d0004db/train/python
"""
class CaesarCipher:
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, shift):
        self.shift = shift

    def encode(self, text):
        res = ""
        for char in text.upper():
            if char in CaesarCipher.ALPHABET:
                char_index = CaesarCipher.ALPHABET.index(char)
                if char_index + self.shift > len(CaesarCipher.ALPHABET) - 1:
                    shifted_index = self.shift - len(CaesarCipher.ALPHABET) + char_index
                else:
                    shifted_index = char_index + self.shift
                res += CaesarCipher.ALPHABET[shifted_index]
            else:
                res += char
        return res

    def decode(self, text):
        res = ""
        for char in text.upper():
            if char in CaesarCipher.ALPHABET:
                char_index = CaesarCipher.ALPHABET.index(char)
                if char_index - self.shift < 0:
                    shifted_index = len(CaesarCipher.ALPHABET) - self.shift + char_index
                else:
                    shifted_index = char_index - self.shift
                res += CaesarCipher.ALPHABET[shifted_index]
            else:
                res += char
        return res


c = CaesarCipher(5) # creates a CipherHelper with a shift of five
print(c.encode('Codewars')) # returns 'HTIJBFWX'
print(c.decode('BFKKQJX')) # returns 'WAFFLES'