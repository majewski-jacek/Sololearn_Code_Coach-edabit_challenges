def snakefill(n):
    space = n * n
    count = 0  

    while True:
        snake = 2** count
        if snake == space:
            return count
            
        elif snake > space:
            return count - 1

        else:
            count += 1 

# https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt