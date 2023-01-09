def semordnilap(words):

    result_arr = []
    while len(words) > 0:
        string1 = words[0]
        new_str = string1[::-1]
        if new_str in words:
            if new_str != string1:
                result_arr.append([string1, new_str])
        words.remove(string1)    
    
    return result_arr
