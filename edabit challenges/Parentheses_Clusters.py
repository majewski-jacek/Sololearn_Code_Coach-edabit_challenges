def split(txt):	
    count_1 = 0
    count_2 = 0
    list_1 = []

    if txt == '':
        return list_1
       
    for i in txt:
        if count_1 == count_2 and count_1 != 0:
            count_1 = 0
            count_2 = 0
            list_1.append(' ')
            list_1.append(i)

            if i == '(':
                count_1 += 1

            else:
                count_2 += 1

        elif i == '(':
            count_1 += 1
            list_1.append(i)

        elif i == ')':
            count_2 += 1
            list_1.append(i)
    
    str = ""
    list_1 = (str.join(list_1))
    result = list(list_1.split(" "))
    return result

# https://edabit.com/challenge/Fpymv2HieqEd7ptAq