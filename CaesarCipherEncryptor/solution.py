def caesarCipherEncryptor(string, key):
    # Write your code here.
    letters = "abcdefghijklmnopqrstuvwxyz"
    key = key % len(letters)
    newString = ""
    for letter in string:
        idx = letters.find(letter)
        position = (idx+key) % len(letters)
        newString += letters[position]
    return newString
