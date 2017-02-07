def func(str):
    i = 0
    y = 0
    splitString = []
    intSet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numberInfo = []
    decoded = ""
    stringLen = len(str)
    while i < stringLen:
        current_char = str[i]
        splitString.append(current_char)
        if any(x in current_char for x in intSet):
            numberInfo.append(int(current_char))
        i = i + 1
    print (splitString)
    print (numberInfo)
    #below is not correct, not getting num of char correct
    #not getting character itself correct (takes first char and doesn't update)
    for x in splitString:
        if any(character in x for character in intSet):
            decodedValue = (splitString[y+1])
            nextIndex = int((splitString[y]))
            decoded = decoded + decodedValue
        else:
            y = y + nextIndex
    print (decoded)
