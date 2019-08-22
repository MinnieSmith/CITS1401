def bitshift(s, k, b):
    string = []
    newString = []
    length = len(s)
    print(length)

    for x in s:
        string.append(x)

    if (b == True):
        for i in string:
            newString[i] = string[((i+k) % length)]
        return newString
    else:
        for i in string:
            newString[((i+k) % length)] = string[i]
        return newString

print (bitshift("100100", 1, True))