def closest_key(dictionary, input_value):
    closest = None
    min_distance = float('inf')  
    for key, values in dictionary.items():
        if values:
            first_element = values[0]
            distance = abs(ord(input_value) - ord(first_element))
            if distance < min_distance:
                min_distance = distance
                closest = key

    return closest
