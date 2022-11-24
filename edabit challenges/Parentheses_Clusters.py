def split(txt):	
    count_1, count_2 = 0, 0    
    result = []

    if txt == '':
        return result
         
    for i in txt:
        if count_1 == count_2 and count_1 != 0:
            count_1, count_2 = 0, 0    
            result.append(' ')
            result.append(i)

            if i == '(':
                count_1 += 1

            else:
                count_2 += 1

        elif i == '(':
            count_1 += 1
            result.append(i)

        elif i == ')':
            count_2 += 1
            result.append(i)
    
    result = "".join(result)
    result = list(result.split(" "))
    return result

# https://edabit.com/challenge/Fpymv2HieqEd7ptAq