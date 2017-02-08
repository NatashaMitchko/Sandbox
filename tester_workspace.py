def plaintext(str):
    i = 0
    y = 0
    intSet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    decoded = ""
    stringLen = len(str)
    print (stringLen)
    while i < stringLen:
        current_char = str[i]
        if any(x in current_char for x in intSet):
            i = int(current_char) + i + 1
            decoded = decoded + str[i]
            i = i + 1
        else:
            i = i + 1
    print (decoded)
