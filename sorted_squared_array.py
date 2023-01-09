def sortedSquaredArray(array):
    new_array = []

    smallest_num_ptr = 0
    largest_num_ptr = len(array)-1
    
    while smallest_num_ptr != largest_num_ptr:
        if abs(array[smallest_num_ptr])>abs(array[largest_num_ptr]):
            new_array.insert(0,array[smallest_num_ptr]**2)
            smallest_num_ptr += 1
        else:
            new_array.insert(0,array[largest_num_ptr]**2)
            largest_num_ptr -= 1
    
    new_array.insert(0,array[smallest_num_ptr]**2)
    return new_array
