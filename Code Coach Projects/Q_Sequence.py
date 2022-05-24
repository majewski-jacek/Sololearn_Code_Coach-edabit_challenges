import functools


# Without functools the function will not be optimized and will fail test 3 and test 4
@functools.lru_cache()
def seq_Q(n):

    if n == 1:
        return 1

    if n == 2:
        return 1
    
    else:
        return seq_Q(n - seq_Q(n - 1)) + seq_Q(n - seq_Q(n - 2))


print(seq_Q(int(input())))

