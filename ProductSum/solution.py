def productSum(array, depth=1):
    # Write your code here.
    sumB = 0
    for i in array:
        if type(i) is int:
            sumB += i
        else:
            sumB += productSum(i, depth+1)
    return sumB*depth
