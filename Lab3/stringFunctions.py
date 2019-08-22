message = "Python rules!"

def listOfWords(string):
    return (string.split())

def stringtoUpper(string):
    return (string.upper())

def locatePosition(string, substring):
    return (string.find(substring))

def replaceSubstring(string, substringold, substringnew):
    return(string.replace(substringold, substringnew))

print(listOfWords(message))
print(stringtoUpper(message))
print(locatePosition(message, "rules"))
print(replaceSubstring(message,"!", "?"))