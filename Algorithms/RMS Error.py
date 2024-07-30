def calculate_rmse(y_pred, y_true):
    import math
    diff = 0
    n = len(y_pred)
    
    if n != len(y_true):
        raise ValueError("The length of y_pred and y_true must be the same.")
    
    for i in range(n):
        diff += (y_pred[i] - y_true[i]) ** 2
    
    mean_squared_error = diff / n
    return math.sqrt(mean_squared_error)
