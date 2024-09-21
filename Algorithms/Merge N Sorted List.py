def sort_lists(lists):
    # Initialize an empty list to hold the combined results
    combined = []
    # Initialize pointers for each list
    pointers = [0] * len(lists)

    while True:
        # Find the smallest current element from the lists
        min_val = float('inf') 
        min_index = -1 # After coming out of the for loop reset min_index = -1
        # If the end of the list is reached min_index = -1 

        for i in range(len(lists)):
            if pointers[i] < len(lists[i]):  # Check if pointer is within bounds
                if lists[i][pointers[i]] < min_val:
                    min_val = lists[i][pointers[i]] # Find the minimum value from all lists
                    min_index = i
        
        # If no valid min_index was found, all lists are fully traversed
        if min_index == -1:
            break

        # Append the smallest value to the combined list
        combined.append(min_val)
        # Move the pointer for the list from which the min value was taken
        pointers[min_index] += 1

    return combined


# DRY RUN 
# Iteration 1:

# min_val = 0, min_index = 3
# Append 0 to combined: combined = [0]
# Increment pointer for list 3: pointers = [0, 0, 0, 1]

# Iteration 2:
# min_val = 1, min_index = 0
# Append 1 to combined: combined = [0, 1]
# Increment pointer for list 3: pointers = [0, 0, 0, 2]

.......

# Iteration 16: 
# Append 12 from list 2 
# combined = [0, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 12]
# pointers = [4, 4, 4, 4]
