def threeNumberSum(array, targetSum):
    # Write your code here.
    results = []
    array.sort()
    for i in array:
        newArray = array.copy()
        newArray.remove(i)
        newSum = targetSum - i
        partialResult = twoNumberSum(newArray, newSum)
        if partialResult != []:
            for j in range(len(partialResult)):
                partialResult[j].insert(0,i)
                partialResult[j].sort()
                if partialResult[j] in results:
                    pass
                else:
                    results.append(partialResult[j])
    return results

def twoNumberSum(array, targetSum):
    reverseArray = []
    result = []
    for i in array:
        reverseArray.append(targetSum-i)
    for i in range(len(reverseArray)):
        if (reverseArray[i] in array) and (reverseArray[i]!=array[i]):
            result.append([array[i], reverseArray[i]])
    result.sort()
    return result