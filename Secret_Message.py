class Logic(object):

    def print_reverse(self, word):
        self.word = word        
        word = word.lower()
        middle = (ord("a") + ord("z"))//2 
        
        for c in word:
            if ord("a") <= ord(c) <= ord("z"):
                c_value = ord(c) + 1 + (middle - ord(c)) * 2
                print(chr(c_value), end="")
            else:
                print(c, end="")

log = Logic()
log.print_reverse(input())