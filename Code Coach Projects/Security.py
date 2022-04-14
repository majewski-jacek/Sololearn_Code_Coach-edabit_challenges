input = str(input())
x = input.replace('x', '')
count = 0

for i in x:
    if count == 2:
        print("ALARM")
        break

    elif i == 'G':
        count = 0

    elif i == '$' or 'T':
        count += 1


if count < 2:
    print('quiet')