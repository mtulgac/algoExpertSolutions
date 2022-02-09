def sortedSquaredArray(array):
    # Write your code here.
    newArray = []
    for j in range(len(array)-1,-1,-1):
        element = array[j]
        if len(newArray) == 0:
            newArray.append(element**2)
        else:
            idx = len(newArray)-1
            while newArray[idx] > element**2 and idx >= 0:
                idx = idx-1
            newArray.insert(idx+1, element**2) 
    return newArray
