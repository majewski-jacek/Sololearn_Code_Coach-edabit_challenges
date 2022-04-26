cards = input().split()

Values_card = { "2": 10,
                "3": 11,
                "4": 12,
                "5": 13,
                "6": 14,
                "7": 15,
                "8": 16,
                "9": 17,
                "1": 18,
                "J": 19,
                "Q": 20,
                "K": 21,
                "A": 22
}

# Changing card value into num
value_cards = []
suits = []
for i in range(len(cards)):
    value_cards.append(Values_card.get(cards[i][0]))
    suits.append(cards[i][-1])

a_cards = sorted(value_cards)

def count_same_values(list_):
   dict = {i:list_.count(i) for i in list_}
   all_values = list(dict.values())
   result = sorted(all_values)
   return result

def same_values(list):
    result = list.count(list[0]) == len(list)

    return result

def consecutive_values(list):
   min_val = min(list)
   max_val = max(list)
   if max_val - min_val + 1 == len(list):
      for i in range(len(list)):
         if list[i] < 0:
            j = -list[i] - min_val
         else:
            j = list[i] - min_val
            if list[j] > 0:
               list[j] = - list[j]
            else:
               return False
      return True
   return False


# Royal Flush bool
bool = [18, 19, 20, 21, 22]
if a_cards == bool and same_values(suits):
    print("Royal Flush")

# Poker bool
elif consecutive_values(a_cards) and same_values(suits):
    print("Poker")


# Four of a Kind bool
elif 4 in count_same_values(a_cards):
   print("Four of a Kind")

# Full House bool
elif [2, 3] == count_same_values(a_cards):
   print("Full House")

# Flush bool
elif 5 in count_same_values(suits):
   print("Flush")

# Straight bool
elif consecutive_values(a_cards):
   print("Straight")

# Three of a Kind bool
elif 3 in count_same_values(a_cards):
   print("Three of a Kind")

# Two Pairs bool
elif [1, 2, 2] == count_same_values(a_cards):
   print("Two Pairs")

# One Pair bool
elif 2 in count_same_values(a_cards):
   print("One Pair")

# High card bool 
else:
   print("High Card")

