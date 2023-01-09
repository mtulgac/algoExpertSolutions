def moveElementToEnd(array, toMove):

    limit = len(array)
    counter = 0

    if len(array) == 0:
        return []
    
    while counter != limit-1:
        if array[counter] == toMove:
            array.pop(counter)
            array.insert(len(array),toMove)
            counter -= 1
            limit -= 1
        counter += 1
    return array