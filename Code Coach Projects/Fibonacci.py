num = int(input())

list = []

def fibonacci(n):
    for i in range(n):
        if i == 0:
            list.append(i)
            print(list[i])

        elif i == 1:
            list.append(i)
            print(list[i])

        elif i > 1:
            list.append(list[i-1] + list[i-2])
            print(list[i])

fibonacci(num)