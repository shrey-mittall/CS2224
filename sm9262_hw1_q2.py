def shift(lst, k, direction = 'left'):
    if(direction == 'right'):
        lst[:] = lst[len(lst)-k:] + lst[:len(lst)-k];
    else:
        lst[:] = lst[k:] + lst[:k];
