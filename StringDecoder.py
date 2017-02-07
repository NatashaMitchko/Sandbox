# Natasha Mitchko
# Python
# Coding Challenge Hackbright Application

def plaintext (str):
    print splitList(str);
    return

def splitList (str):
    i = 0;
    int stringLength = len(str);
    intSet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
    global splitString = [];
    #global indexArray = [];

#create list with string split into characters and stored in correct data types
    while i < stringLength:
        character = str[i]
            if any(x in character for x in intSet):
                integerFromString = int(str[i])
                splitString.append(integerFromString);
            else:
                splitString.append(character)
            i = i + 1
    return splitString
