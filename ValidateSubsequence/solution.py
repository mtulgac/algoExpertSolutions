def isValidSubsequence(array, sequence):

    for s in sequence:
        if s in array:
            index = array.index(s)
            array = array[index+1:]
        else:
            return False
    return True