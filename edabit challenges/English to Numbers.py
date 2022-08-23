def eng2nums(s):
    dict = {
            "zero":0,
            "one":1,
            "two":2,
            "three":3,
            "four":4,
            "five":5,
            "six":6,
            "seven":7,
            "eight":8,
            "nine":9,
            "ten":10,
            "eleven":11,
            "twelve":12,
            "thirteen":13,
            "fourteen":14,
            "fifteen":15,
            "sixteen":16,
            "seventeen":17,
            "eighteen":18,
            "nineteen":19,
            "twenty":20,
            "thirty":30,
            "forty":40,
            "fifty":50,
            "sixty":60,
            "seventy":70,
            "eighty":80,
            "ninety":90
    }

    word = s.split()
    res = 0
    try:
        if word[1] == "hundred":
            res += dict[word[0]]
            res *= 100
            for x in range(2, len(word)):
                res += dict[word[x]]        
        else:
            for x in range(len(word)):
                res += dict[word[x]]
    except IndexError:
        res += dict[word[0]]

    return res

# https://edabit.com/challenge/9cuQrhEMwiESfKznk