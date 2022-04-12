class log(object):

    def __init__(self, sign):
        self.sign = sign

    def fun(self):
        count = 0
        for i in password:
            if i in self.sign:
                count += 1
            if count == 2:
                return True
        else:
            return False


password = input()
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special_characters = ['!', '@', '#', '$', '%', '&', '*']

l_num = log(numbers)
bool_1 = l_num.fun()

l_spec = log(special_characters)
bool_2 = l_spec.fun()


if bool_1 and bool_2 and len(password) >= 7:
    print("Strong")
else:
    print("Weak")
