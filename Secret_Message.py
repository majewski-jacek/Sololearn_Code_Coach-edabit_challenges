# Convert input to list
Uncoded_message = input()
list_1 = []
list_1[:0] = Uncoded_message.lower()

# Decoding
list_2 = []
for char in list_1:
    dec_char = ord(char)
    list_2.append(dec_char)

# Reversing character and encoding // len == 32 is 'space'
list_3 = []
count_1 = 0
for len in list_2:
    count = 0
    if len == 32:
        list_3.append(chr(len))
    for DEC in range(97, 123):       
        if DEC == list_2[count_1]:            
            if DEC < 112:
                DEC = 122 - count
                list_3.append(chr(DEC))
                break
            if DEC >= 112:
                DEC = 122 - count
                list_3.append(chr(DEC))
                break
        count += 1
    count_1 += 1

# Convert list to string
def List_To_String(list):     
    string = ""     
    for element in list: 
        string += element       
    return string 

# Print result
print(List_To_String(list_3))


