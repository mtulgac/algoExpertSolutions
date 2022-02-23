def insertionSort(array):
    # Write your code here.
    sortedArray = []
    sortedArray.append(array[0])

    for i in range(1, len(array)):
        idx = len(sortedArray)
        while array[i] < sortedArray[idx-1] and idx!=0:
            idx -= 1
        sortedArray.insert(idx,array[i])

    return sortedArray