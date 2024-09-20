# Intuition :
# Two rectangles do not overlap if one is entirely to the left, right, above, or below the other. 
# In such a case, they will be separated along the x-axis or y-axis.

def rectangle_overlap(a, b) -> bool:
    # X and Y points for rectangel a and b 
    x_a = [point[0] for point in a]
    y_a = [point[1] for point in a]
    
    x_b = [point[0] for point in b]
    y_b = [point[1] for point in b]
    
    # Boundaries of rectangle a
    min_x_a = min(x_a)
    max_x_a = max(x_a)
    min_y_a = min(y_a)
    max_y_a = max(y_a)
    
    # Boundaries of rectangle b
    min_x_b = min(x_b)
    max_x_b = max(x_b)
    min_y_b = min(y_b)
    max_y_b = max(y_b)
    
    # Check if there is no overlap
    if max_x_a < min_x_b or max_x_b < min_x_a:
        return False  # No overlap along the x-axis
    
    if max_y_a < min_y_b or max_y_b < min_y_a:
        return False  # No overlap along the y-axis
    
    # If no separation found along both axes, the rectangles overlap
    return True
