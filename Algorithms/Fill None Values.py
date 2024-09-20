# Solution 1 Using Stack 
def fill_none(input_list):
    stk = [0] # Initialize as zero for the case when first value in the list is None 
 
    for i,n in enumerate(input_list):
        if n is not None:
            stk.append(n)
        else:
            input_list[i] = stk[-1]
    return input_list

# Solution 2 Without Stack
def fill_none(input_list):
    prev_value = 0
    for i, n in enumerate(input_list):
        if n is not None:
            prev_value = n
        else:
            input_list[i] = prev_value
    return input_list
