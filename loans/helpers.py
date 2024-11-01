import math

def is_prime(number):
    if number < 1:
        raise ValueError

    if number == 1:
        return False
    
    for factor in range(2, int(math.sqrt(number)) + 1):
        if number % factor == 0:
            return False
    
    return True