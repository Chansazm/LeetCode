def buildString(s):
    arr = []
    
    for c in s:
        arr.append(c)
    return "".join(arr)


string = " I love you"

print(buildString(string))