def getNthFib(n):
    if n == 1:
        return 0
    else:
        fibonnacciList = [0]*n
        fibonnacciList[0] = 0 
        fibonnacciList[1] = 1 
        for i in range(2,n):
            fibonnacciList[i] = fibonnacciList[i-1] + fibonnacciList[i-2]
        return fibonnacciList[n-1]
