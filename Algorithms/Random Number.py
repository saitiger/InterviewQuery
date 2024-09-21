import random
def random_number(x, y=0, count=1):
    # For the first element, select it with probability 1
    if count == 1:
        return x
    # For subsequent elements, select the new element with probability 1/count
    if random.randint(1, count) == 1:
        return x
    return y

# Reservoir Sampling : 
https://www.geeksforgeeks.org/reservoir-sampling/
