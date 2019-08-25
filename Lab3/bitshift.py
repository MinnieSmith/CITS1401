def bitshift(s, k, b):
    string = []

    for x in s:
        string.append(x)

    length = len(string)

    if b == True:
        for i in range(k):
            x = string.pop(0)
            string.insert(length - 1, x)
        print("".join(string))

    if b == False:
        for i in range(k):
            x = string.pop(-1)
            string.insert(0, x)
        print("".join(string))


bitshift("1000000", 1, True)
bitshift("1000000", 2, False)
bitshift("1000000", 3, False)
bitshift("1000000", 4, False)

