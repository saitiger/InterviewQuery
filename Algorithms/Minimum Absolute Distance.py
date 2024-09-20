def min_distance(test_input):
    test_input.sort()
    min_distance = float('inf')
    
    # Traverse the array to find the minimum in distance in the array 
    for i in range(1,len(test_input)):
        if test_input[i]-test_input[i-1]<min_distance:
            min_distance = test_input[i]-test_input[i-1]
          
    # Append those pairs which have the same distance as the minimum distance
    res = []
    for i in range(1,len(test_input)):
        if test_input[i]-test_input[i-1]==min_distance:
            res.append([test_input[i-1],test_input[i]])

    return res 
