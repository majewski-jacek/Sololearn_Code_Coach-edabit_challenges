def Convert(sentence):
    for word in sentence:
        result = word[1:] + word[0] + 'ay' + ' '
        print(result, end="")

Convert(input().split())
