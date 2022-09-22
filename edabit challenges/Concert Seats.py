def can_see_stage(seats):
    reset_count = 1
    results = []
    items_to_return = []

    # Loop for a vertical row
    for count in range(len(seats)):
        for seat in seats:
            results.append(seat[count])
            # Statment that check everyone can see the front-stage 
            if reset_count == len(seats) and results == sorted(results) and len(set(results)) == len(results):
              results.clear()
              reset_count = 1
              items_to_return.append(True)
            else:
              reset_count += 1

    if len(items_to_return) == len(seats):
      return True
    else:
      return False

# https://edabit.com/challenge/xbjDMxzpFcsAWKp97