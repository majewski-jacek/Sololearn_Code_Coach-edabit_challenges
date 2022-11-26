def advanced_sort(lst):
    SortedList = sorted(lst, key=lambda x: lst.index(x))
    Outer = []
    Index = 0
    LenList = len(SortedList)

    while Index < LenList:
        Value = SortedList[Index]
        Inner = [Value]
        
        # Inner loop increments Outer Index in case of same values
        for i in range(Index+1, len(SortedList)):
            Candidate = SortedList[i]
            if Candidate == Value:
                Index +=1
                Inner.append(Candidate)
            else:
                break
            
        Outer.append(Inner)
        Index +=1
        
    return Outer

# https://edabit.com/challenge/6vSZmN66xhMRDX8YT