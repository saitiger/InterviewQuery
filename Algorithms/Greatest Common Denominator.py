def gcd_two_numbers(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd_two_numbers(result, num)
    return result
