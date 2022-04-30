class Log(object):
    def __init__(self, answer, expres):
        self.answer = answer
        self.expres = expres
        self.list = []

    def rem_tpl(self):
        for i in self.expres:
            self.list.append(i[1:-1])
        return self.list 

    def index_res(self):
        count = 0
        for i in self.list:
            if eval(i) == self.answer:
                return f"index {count}"
            count += 1
    
        return "none"


x = int(input())
y = input().split()

L = Log(x, y)
L.rem_tpl()
print(L.index_res())