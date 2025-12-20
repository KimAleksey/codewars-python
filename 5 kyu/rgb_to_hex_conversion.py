"""
https://www.codewars.com/kata/513e08acc600c94f01000001
"""

from dataclasses import dataclass

@dataclass
class RGB:
    r: int
    g: int
    b: int

    def __post_init__(self) -> None:
        """
        Check if input is valid.
        :return: None
        """

        if not all(isinstance(i, int) for i in (self.r, self.g, self.b)):
            raise TypeError("Input must be integers")

    @staticmethod
    def convert_int_to_hex(i: int) -> str:
        """
        Int formated to 2 characters with leading zeros.
        :param i: int
        :return: hex
        """

        clamped = min(max(i, 0), 255)
        return f"{clamped:02X}"

    def to_hex(self):
        hex_colors = "".join(self.convert_int_to_hex(i) for i in (self.r, self.g, self.b))
        return hex_colors


print(RGB(1, 275, 125).to_hex())