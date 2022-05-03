class Log(object):
    def __init__(self, map):
        self.map = map
        self.col_P = []
        self.valcol_P = []
        self.place_P = []
        self.count = 0

    def list(self):
        self.count = 0
        for i in self.map:
            if "P" in i:
                self.col_P.append(i)
                self.valcol_P.append(self.count)
            self.count += 1
        return self.col_P, self.valcol_P

    def one_hor_col(self, floor):  
        self.count = 0
        for i in floor:
            if i == "P":
                self.place_P.append(self.count)
            self.count += 1
        return self.place_P[1] - self.place_P[0]

    def hor_col(self, floor):    
        self.count = 0
        for i in floor:
            if i == "P":
                return self.count
            self.count += 1

    def calc(self, pos1, pos2):
        res = pos1 - pos2
        if res < 0:
            return res * -1
        return res


L = Log(input().split(","))
L.list()

try:
    x = L.hor_col(L.col_P[1])
    y = L.hor_col(L.col_P[0])
    print(L.calc(x, y) + L.valcol_P[1] - L.valcol_P[0])

# If two "P" in same tier
except IndexError:
    print(L.one_hor_col(L.col_P[0]))