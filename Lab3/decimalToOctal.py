def decimalToOctal(decimal):
    s = str(decimal)
    n = len(s)
    deci = []
    sum = 0
    d = 0

    for i in range(n):
        x = int(decimal / (8 ** i) % 8)
        deci.append(x)

    for k in deci:
        sum = sum + (k * 10 ** (d))
        d += 1
    return sum


print(decimalToOctal(214))
