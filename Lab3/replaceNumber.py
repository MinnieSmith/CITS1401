
def replaceNumber(string, substring, newsubstring):
    s = string.lower()
    t = substring.lower()
    u = newsubstring.lower()

    print(s.replace(t, u))

replaceNumber("Ten is ten is TEN is TeN", "Ten", "ten(10)")




