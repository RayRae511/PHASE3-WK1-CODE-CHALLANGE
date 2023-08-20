def two_positives(r,a,y):
    # Counts the number of positive integers
    count = 0
    if r > 0:
        count += 1
    if a > 0:
        count += 1
    if y > 0:
        count += 1
        
    # Checks if exactly two integers are positive
    if count == 2:
        return True
    else:
        return False