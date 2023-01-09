def firstNonRepeatingCharacter(string):

    new_dict = {}
    for i in range(len(string)):
        new_dict[string[i]] = 0

    for i in range(len(string)):
        new_dict[string[i]] += 1

    for i in range(len(string)):
        if new_dict[string[i]] == 1:
            return i
    
    return -1
