def Convert(sentence):
    for word in sentence:
        ch_1 = word[0]
        result = word[1:]  + word[0] + 'ay' + ' '
        print(result, end="")

Convert(input().split())
