def nonConstructibleChange(coins):
    # Write your code here.
    if len(coins) == 0:
        return 1
    else:
        result = 0
        coins.sort()
        for c in coins:
            if c > result+1:
                return result + 1 
            else:
                result += c
    return result + 1