def runLengthEncoding(string):
    # Write your code here.
    newString = []	
    counter = 1
    if len(string) == 1:
        return "1{}".format(string[0])
    for i in range(1, len(string)):
        if i != len(string)-1:
            if string[i] == string[i-1]:
                counter += 1
                if counter == 9:
                    newString.append(str(counter))
                    newString.append(string[i])
                    counter = 0
            else:
                if counter != 0:
                    newString.append(str(counter))
                    newString.append(string[i-1])
                    counter = 1
                else:
                    counter = 1
        else:
            if string[i] == string[i-1]:
                counter += 1
                newString.append(str(counter))
                newString.append(string[i])
            else:
                newString.append(str(counter))
                newString.append(string[i-1])
                newString.append(str(1))
                newString.append(string[i])
    return "".join(newString)