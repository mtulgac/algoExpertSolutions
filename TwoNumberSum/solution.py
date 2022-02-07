def twoNumberSum(array, targetSum):
    # Write your code here.
    reverseArray = []
	result = []
	for i in array:
		reverseArray.append(targetSum-i)
	for i in range(len(reverseArray)):
		if (reverseArray[i] in array) and (reverseArray[i]!=array[i]):
			result = [array[i], reverseArray[i]]
	return result