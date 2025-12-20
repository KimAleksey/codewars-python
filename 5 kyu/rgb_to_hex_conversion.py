def rgb(r: int, g: int, b: int) -> str:
    """
    RBL as input must be integers. Output is color in HEX format in str.

    :param r: red
    :param g: green
    :param b: blue
    :return: Color in HEX format
    """
    if not any(isinstance(i, int) for i in (r, g, b)):
        raise TypeError("Input must be integers")

    def convert(i: int) -> str:
        clamped = min(max(i, 0), 255)

        return f"{clamped:02X}"

    hex_colors = [convert(i) for i in (r, g, b)]

    return "".join(hex_colors)


print(rgb(-20, 275, 125))