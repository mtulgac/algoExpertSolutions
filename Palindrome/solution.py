def isPalindrome(string):
    # Write your code here.
    if len(string) == 1:
        return True
    else:
        firstPtr = 0
        lastPtr = len(string)-1
        for i in range(len(string)):
            if string[firstPtr+i] != string[lastPtr-i]:
                return False
    return True
