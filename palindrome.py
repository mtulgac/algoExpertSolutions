def isPalindrome(string):

    first_ptr = 0
    last_ptr = len(string)-1
    while first_ptr < last_ptr:
        if string[first_ptr] != string[last_ptr]:
            return False
        else:
            first_ptr += 1
            last_ptr -= 1
    return True
