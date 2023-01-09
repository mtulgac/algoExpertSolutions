def minimumWaitingTime(queries):
    
    queries.sort()
    sum = 0
    total_sum = 0
    
    for i in range(len(queries)-1):
        sum += queries[i]
        total_sum += sum
    return total_sum
