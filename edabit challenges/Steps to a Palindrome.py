def min_palindrome_steps(txt):
    reverse_txt = txt[::-1]
    steps = 0

    while True:
        if txt == reverse_txt:
            return steps
        
        else:
            txt = txt[1:]
            reverse_txt = reverse_txt[:-1]
            steps += 1


# https://edabit.com/challenge/WyttgdGuQGaRBqhhP