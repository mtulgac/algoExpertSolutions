def firstDuplicateValue(array):

    array_freq = {}
    for i in array:
        array_freq[i] = 0

    for i in array:
        array_freq[i] += 1
        if array_freq[i] == 2:
            return i
    return -1  