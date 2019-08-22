def octalToDecimal(octal):
    s = str(octal)
    n = len(s)
    octi = []
    sum = 0
    o = 0

    for i in range(n):
        x = int(octal / (10 ** i) % 10)
        octi.append(x)

    for k in octi:
        sum = sum + (k * 8 ** (o))
        o += 1
    return sum


print(octalToDecimal(326))
