def extractSubstring(string, substring):
    firstposition = int(string.find(substring))
    lenSubstr = int(len(substring))

    if (firstposition != -1):
        print(firstposition, lenSubstr)
        finalPos = firstposition + lenSubstr
        newString = string[firstposition: finalPos]
        return newString
    else:
        return print("substring not found")

def removeSubstring(string, substring):
    return string.replace(substring, "")

def extractMiddleChar(string):
    midchr = int(len(string)/2)
    return string[midchr:midchr+1]


print(extractSubstring("myprogram.exe", "gram"))
print(removeSubstring("myprogram.exe", ".exe"))
print(extractMiddleChar("myprogram.exe"))