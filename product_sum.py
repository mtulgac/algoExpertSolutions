
def productSum(arr, current_depth=1):

    sum = 0
    for i in range(len(arr)):
        if type(arr[i])==int:
           sum += arr[i]
        else:
           sum += productSum(arr[i], current_depth+1)
    return sum*current_depth