# Turns a message into the ascii number
def caesarEncode(message):
    asciimsg = []
    # turn each letter into lowercase
    lwrmsg = message.lower()
    # Loops through message and turns each character into a number
    # and stores it in asciimsg array
    for ch in lwrmsg:
        asciimsg.append(ord(ch))

    return asciimsg


# loops through and shifts the asciimsg to all possible 26 positions
def caesarShift(asciimsg):
    shiftmsg = []
    allpsblshiftmsg = []
    n = 1
    a = 97
    z = 122
    sum = 0
    while (n <=26):
        for num in asciimsg:
            sum = a + ((num + n -a) % 26)
            shiftmsg.append((sum))
        allpsblshiftmsg.append(shiftmsg)
        n += 1
    return allpsblshiftmsg



# Decodes all the possible ascii shift combinations into characters
def caesarDecode(shiftedasciimsg):
    decodedmsg = ""
    s = 0

    for i in range(len(shiftedasciimsg)):
        for j in range(len(shiftedasciimsg[i])):
            s = shiftedasciimsg[i][j]
            decodedmsg = decodedmsg + chr(s)
    return decodedmsg

# Splits the decoded string into the length of the original encoded message
# to make it easier to figure which was the original message

def splitDecode(decodedmsg, length):
    return [decodedmsg[i:i+length] for i in range(0, len(decodedmsg), length)]



x = caesarEncode("Minh")
s = caesarShift(x)
t = caesarDecode(s)
u = splitDecode(t, 4)


print(u)