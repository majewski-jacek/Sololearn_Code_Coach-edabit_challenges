def profit(info):
    Total_Sales = info['sell_price'] * info['inventory']
    Total_Cost = info['cost_price'] * info['inventory']
    Profit = Total_Sales - Total_Cost
    return round(Profit)

# https://edabit.com/challenge/YfoKQWNeYETb9PYpw