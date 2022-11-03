

def convert_binary(binary: list[str], base: str):
    # start by converting to decimal
    content = "{0:" + base + "}"
    return content.format(int(''.join(binary), 2))


if __name__ == '__main__':
    # binary representation of 100 is 1100100
    number = convert_binary(['1', '1', '0', '0', '1', '0', '0'], 'x')
    print(number)
