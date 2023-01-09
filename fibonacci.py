def getNthFib(n):
    x = 0
    y = 1
    if n == 1:
        return x
    elif n == 2:
        return y

    else:
        for i in range(2,n):
            f_n = x+y
            x = y
            y = f_n 
        return f_n
