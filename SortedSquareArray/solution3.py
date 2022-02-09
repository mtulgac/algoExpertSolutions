def sortedSquaredArray(array):
    # Write your code here.
    newArray = [j**2 for j in array]
    newArray.sort()
    return newArray