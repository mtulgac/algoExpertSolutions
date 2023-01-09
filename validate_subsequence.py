def isValidSubsequence(array, sequence):

    idx = 0
    new_seq = []
    for i in range(len(array)):
        if array[i] == sequence[idx]:
            new_seq.append(array[i])
            idx += 1
            if idx == len(sequence):
                return True
    return False