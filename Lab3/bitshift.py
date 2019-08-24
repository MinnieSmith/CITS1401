def bitshift(s, k, b):
    string = []

    length = len(s)
    print(length)

    for x in s:
        string.append(x)
    print(string)

    if b == False:
        for i in range(k):
            string[-k] = string[i]
        print(string)


bitshift("101100", 1, False)

bitshift("100001", 2, False)
    # if b == True:
    #     for i in range(length):
    #         string[i], string[-k] = string[-k], string[-i]
    #     print(string)







    # for i in range(length):
    #     string[i] = string[(i + k) % length]
    # print(string)

    # if (b == True):
    #     for i in string:
    #         newString.append(string[((i+int(k)) % length)])
    #     return newString
    # else:
    #     for i in string:
    #         newString[((i+int(k)) % length)] = string[i]
    #     return newString



