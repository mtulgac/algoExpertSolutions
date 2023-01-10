def caesarCipherEncryptor(string, key):

    maxValue = ord("z")
    startValue = ord("a")
    new_string = ""
    key = key % 26
    for char in string:

        unicode_value = ord(char)
        if unicode_value + key > maxValue:
            new_value = (unicode_value + key) - maxValue + startValue-1
            new_string += (chr(new_value))
        else:
            new_value = (unicode_value + key)
            new_string += (chr(new_value))

    return new_string
