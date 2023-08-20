def highest_consonant_value(r):
    max_val = 0
    current_val = 0
    
    for c in r:
        if c not in 'aeiou':
            current_val = ord(c) - ord('a') + 1
            if current_val > max_val:
                max_val = current_val
        else:
            current_val = 0

    return max_val
#testing the function
'''
r = 'hello'
print(highest_consonant_value(r)) #Output: 8
'''