class Log(object):
    def __init__(self, Map):
        self.Map = Map
        self.Column_P = []
        self.IndexColumn_P = []
        self.Index_P = []
        self.Count = 0

    def index_2Dmap(self):
        self.Count = 0
        for floor in self.Map:
            if "P" in floor:
                self.Column_P.append(floor)
                self.IndexColumn_P.append(self.Count)
            self.Count += 1
        return self.Column_P, self.IndexColumn_P

    def index_one_floor(self, floor):  
        self.Count = 0
        for i in floor:
            if i == "P":
                self.Index_P.append(self.Count)
            self.Count += 1
        return self.Index_P[1] - self.Index_P[0]

    def index_floor(self, floor):    
        self.Count = 0
        for i in floor:
            if i == "P":
                return self.Count
            self.Count += 1

    def calculate(self, pos1, pos2):
        result = pos1 - pos2
        if result < 0:
            return result * -1
        return result


L = Log(input().split(","))
L.index_2Dmap()

try:
    x = L.index_floor(L.Column_P[1])
    y = L.index_floor(L.Column_P[0])
    print(L.calculate(x, y) + L.IndexColumn_P[1] - L.IndexColumn_P[0])

# If two "P" in same floor, for example PXXPX
except IndexError:
    print(L.index_one_floor(L.Column_P[0]))