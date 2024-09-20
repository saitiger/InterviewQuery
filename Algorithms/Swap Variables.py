def swap_values(numbers):
    numbers['a'], numbers['b'] = numbers['b'], numbers['a']
    return numbers

    # Solution 2 
    numbers['a'] += numbers['b']
    numbers['b'] = numbers['a'] - numbers['b']
    numbers['a'] = numbers['a'] - numbers['b']
    return numbers
