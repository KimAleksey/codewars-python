"""
https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python
"""

def rot13(message: str) -> str:
    if not message:
        return ""
    if not isinstance(message, str):
        return ""
    keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    values = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    decipher = dict(zip(keys, values))
    return ''.join(ch if not ch in decipher else decipher[ch] for ch in message)


print(rot13('EBG13 rknzcyr.'))