import string
xd = []
xd[:0] = string.ascii_lowercase
#print(xd)

x = input()
y = x.replace(" ", "")
#print(y)

def Convert(string):
    list1 = []
    list1[:0] = string
    list = list1[::-1]
    return list
z = Convert(y)
#print(z)

count = 0
for char in z:
    if char == xd[count]:
        print(char)
    count += 1

