def func(str):
    i = 0
    splitString = []
    intSet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    indexInfo = []
    decoded = ""
    stringLen = len(str)
    while i < stringLen:
        current_char = str[i]
        splitString.append(current_char)
        if any(x in current_char for x in intSet):
            indexInfo.append(int(current_char))
        i = i + 1
    print splitString
    print indexInfo
    #lots of out of range errors to fix
    for i in indexInfo:
        decoded = decoded + splitString[i]
    print decoded

