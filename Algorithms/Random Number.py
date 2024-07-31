import random

def random_number(x, y=None, count=1):
    count += 1

    if random.randint(1, count) == 1:
        y = x  
      
    return y, count
