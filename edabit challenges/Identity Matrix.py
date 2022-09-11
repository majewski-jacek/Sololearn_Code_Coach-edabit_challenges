def id_mtrx(n):
    try:
        # Indetyfikacja czy podana wartość jest liczbą
        int(n)

        items_to_return = []
        if n > 0:
            for num in range(n):
                items_to_return.append(calculate(n, num))
        
        elif n < 0:
            n *= -1
            for num in range(n):
                items_to_return.append(calculate(n, num))
            items_to_return.reverse()

        return items_to_return

    except ValueError:
        return "Error"


def calculate(n, count):
    floor = []
    if n > 0:
        for num in range(n):
            if num == count:
                floor.append(1)                    
            else:
                floor.append(0)
    
    return floor

# https://edabit.com/challenge/QN4RMpAnktNvMCWwg