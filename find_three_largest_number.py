def findThreeLargestNumbers(array):

    max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')    

    for i in range(len(array)):

        if array[i] > max1:
            max3 = max2
            max2 = max1
            max1 = array[i]

        elif array[i] > max2:
            max3 = max2
            max2 = array[i]

        elif array[i] > max3:
            max3 = array[i]

    return [max3, max2, max1]
            
        

