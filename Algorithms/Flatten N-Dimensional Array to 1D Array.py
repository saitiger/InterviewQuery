def flatten_array(array):
    flat_list = []
    for element in array:
        if isinstance(element, list):
            flat_list.extend(flatten_array(element))
        else:
            flat_list.append(element)
    return flat_list
