def insertionSort(array):
    
    new_array = []
    new_array.append(array[0])
    for i in range(1, len(array)):
        for j in range(0,len(new_array)):
            if array[i] < new_array[j]:
                new_array.insert(j, array[i])
                break
            else:
                if j == len(new_array)-1:
                    new_array.insert(j+1, array[i])
    return new_array
