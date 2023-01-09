def nonConstructibleChange(coins):
    
    current_value = 0
    coins.sort()
    print(coins)
    for i in range(len(coins)):
        if coins[i] > current_value+1:
            break
        else:
            current_value += coins[i]
    return current_value+1

