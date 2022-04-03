# zmienne
count_input = int(input())
sum = 0

# pętla do sumowania parzystych liczb
for i in range(count_input):
    val = int(input())
    if val % 2 == 0:
        sum += int(val)

print(sum)
