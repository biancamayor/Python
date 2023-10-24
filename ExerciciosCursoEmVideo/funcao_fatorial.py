def fatorial(n, show = True):
    f = 1
    for c in range (n, 0, -1):
        if show:
            print(c, end = '')
            if c> 1:
                print('x', end ='')
            else:
                print(f'= {f}', end='')
        f = c*f
    return f
        
fatorial(5, show = True)
