def twoNumberSum(array, targetSum):

    # Defining two arrays for result and comparison
    reverseArray = []
    result = []

    # Appending the required integers for targetSum
    for i in array:
        reverseArray.append(targetSum-i)

    # Checking if any of the required integers are in the original array
    for i in range(len(reverseArray)):
        if (reverseArray[i] in array) and (reverseArray[i]!=array[i]):
            result = [array[i], reverseArray[i]]
    return result