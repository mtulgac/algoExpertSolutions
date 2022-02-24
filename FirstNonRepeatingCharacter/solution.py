def firstNonRepeatingCharacter(string):
    # Write your code here.
    freqs = {}
    for c in string:
        freqs[c] = 0
    for c in string:
        freqs[c] += 1
    for c in range(len(string)):
        if freqs[string[c]] == 1:
            return c
    return -1
