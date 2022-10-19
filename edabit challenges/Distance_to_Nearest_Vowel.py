def distance_to_nearest_vowel(txt):
    count = 0
    vowel_places = []
    Vowels = ['a', 'e', 'i', 'o', 'u']
    
    for i in txt:        
        if i in Vowels:
            vowel_places.append(count)
        count += 1

    count_2 = 0
    result = []
    
    for i in txt:
        distances_from_vowels = []        
        for k in vowel_places:
            distance = count_2 - k
            if distance < 0:
                distance *= -1                
            distances_from_vowels.append(distance)

        count_2 += 1
        result.append(min(distances_from_vowels))
    return result


# https://edabit.com/challenge/jWHkKc2pYmgobRL8R