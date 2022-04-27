class Log(object):
   
    def cards_into_value(self, cards, val_cards):
        value_cards = []
        for i in range(len(cards)):
            value_cards.append(val_cards.get(cards[i][0]))

        value_cards = sorted(value_cards)
        return value_cards

    def suits_in_cards(self, cards):
        suits = []
        for i in range(len(cards)):
            suits.append(cards[i][-1])
        
        suits = sorted(suits)
        return suits

    def count_same_values(self, val_cards_or_suits):
        dict = {i:val_cards_or_suits.count(i) for i in val_cards_or_suits}        
        all_values = list(dict.values())
        result = sorted(all_values)
        return result

    def consecutive_values(self, list_val):
        return sorted(list_val) == list(range(min(list_val), max(list_val)+1))


class Values(object):
    
    Values_card = { "2": 10, "3": 11, "4": 12,                    
                    "5": 13, "6": 14, "7": 15,
                    "8": 16, "9": 17, "1": 18,
                    "J": 19, "Q": 20, "K": 21,
                    "A": 22
                    }


class Bool(object):

    def Bools(self, up_cards, suits):
            royal_flush = [18, 19, 20, 21, 22]
            consecutive_cards = Log().consecutive_values(up_cards)
            count_same_cards = Log().count_same_values(up_cards)
            count_same_suits = Log().count_same_values(suits)
        
            bools_statements = {"Royal Flush": up_cards == royal_flush and 5 in count_same_suits ,
                                "Straight Flush": consecutive_cards and 5 in count_same_suits ,
                                "Four of a Kind": 4 in count_same_cards ,
                                "Full House": [2, 3] == count_same_cards ,
                                "Flush": 5 in count_same_suits ,
                                "Straight": consecutive_cards ,
                                "Three of a Kind": 3 in count_same_cards ,
                                "Two Pairs": [1, 2, 2] == count_same_cards,
                                "One Pair": 2 in count_same_cards,
                                "High Card": True }

            dict_cond = {k:v for (k,v) in bools_statements.items() if v == True}

            # Return a first highest rank 
            return list(dict_cond.keys())[0]


carts_in_hands = input().split()
Values = Values().Values_card
val_cards = Log().cards_into_value(carts_in_hands, Values)
suits = Log().suits_in_cards(carts_in_hands)
print(Bool().Bools(val_cards, suits))
