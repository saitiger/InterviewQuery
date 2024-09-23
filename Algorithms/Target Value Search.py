def target_value_search(rotated_input, target_value):
    left, right = 0, len(rotated_input) - 1

    while left <= right:
        mid = (left + right) // 2
        
        # Check if the middle element is the target
        if rotated_input[mid] == target_value:
            return mid
        
        # Left Rotated or Right Rotated 
        if rotated_input[left] <= rotated_input[mid]:
            # Left side is sorted
            if rotated_input[left] <= target_value < rotated_input[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right side is sorted
            if rotated_input[mid] < target_value <= rotated_input[right]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
