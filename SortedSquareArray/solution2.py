def sortedSquaredArray(array):
    # Write your code here.
    newArray = [0 for a in array]
    startPointer = 0
    endPointer = len(array)-1

    for i in reversed(range(len(array))):
        
        leftValue = array[startPointer]
        rightValue = array[endPointer]
        
        if abs(leftValue) > abs(rightValue):
            newArray[i] = leftValue**2
            startPointer += 1
        else:
            newArray[i] = rightValue**2
            endPointer -= 1

    return newArray
