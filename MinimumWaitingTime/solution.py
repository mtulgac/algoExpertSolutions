def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    result = 0
    for i in range(1,len(queries)):
        result += sum(queries[:i])
    return result