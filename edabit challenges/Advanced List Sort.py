def advanced_sort(lst):
    sort_lst = sorted(lst, key=lambda x: lst.index(x))
    result = []
    while sort_lst:
        list = []
        if len(sort_lst) != 0:
            for i in range(len(sort_lst) + 1):
                try:
                    if i == 0:
                        list.append(sort_lst[i])
        
                    elif sort_lst[0] == sort_lst[1]:
                        list.append(sort_lst[0])
                        sort_lst.pop(0)

                    else:
                        result.append(list)
                        sort_lst.pop(0)
                        list = []
                        break
                
                # Exception for line 14
                except IndexError:
                    result.append(list)
                    return result
        else:
            return result

# https://edabit.com/challenge/6vSZmN66xhMRDX8YT