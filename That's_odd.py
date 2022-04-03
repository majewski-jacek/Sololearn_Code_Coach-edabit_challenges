# zmienne
count_input = int(input())
even_numbers = ['0', '2', '4', '6', '8']
sum = 0

# pętla do sumowania parzystych liczb
for i in range(count_input):
    val = int(input())
    if val % 2 == 0:
        sum += int(val)

print(sum)
