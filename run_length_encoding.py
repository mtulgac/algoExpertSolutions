def runLengthEncoding(string):

    result_str = ''
    current_char = string[0]
    counter = 1
    
    for i in range(len(string)-1):
        if string[i+1] == current_char:
            counter += 1    
            if counter == 9:
                result_str += '{}'.format(str(counter)+current_char)
                current_char = string[i+1]
                counter = 0
        else:
            if counter == 0:
                current_char = string[i+1]
                counter =1
            else:
                result_str += '{}'.format(str(counter)+current_char)
                current_char = string[i+1]
                counter = 1

    result_str += '{}'.format(str(counter)+current_char)
    return result_str
