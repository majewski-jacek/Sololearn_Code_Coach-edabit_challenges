months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

US_date = input()

try:
    z = US_date.replace(' ', ',')
    conv_date = z.split(',')
    if conv_date[2] == '':
        del conv_date[2]

    month = conv_date[0]
    day = conv_date[1]
    year = conv_date[2]
    if any([i == month for i in months]):
        print(f"{day}/{months[month]}/{year}")

except:
    x = US_date.split('/')
    month = x[0]
    day = x[1]
    year = x[2]
    print(f"{day}/{month}/{year}")
