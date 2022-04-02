# zmienne
count_input = int(input())
even_numbers = ['0', '2', '4', '6', '8']
sum = 0

# pętla do sumowania parzystych liczb
for i in range(count_input):
    val = input()
    val_1 = val[-1]
    if val_1 in even_numbers:
        sum += int(val)

print(sum)
