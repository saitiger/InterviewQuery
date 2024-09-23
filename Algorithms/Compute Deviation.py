import math
def compute_deviation(input_data):
    result = {}
    for item in input_data:
        key = item['key']
        values = item['values']
        mn = sum(values) / len(values)
        var = sum((x - mn) ** 2 for x in values) / len(values)
        std_dev = math.sqrt(var)
        result[key] = std_dev
    return result
