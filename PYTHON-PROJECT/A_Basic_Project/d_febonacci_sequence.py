def fibonacci_sequence(max_num):
    a, b = 0, 1
    result = f"{a} +{b}"
    total = a + b
    while total <= max_num:

        a, b = b, a + b
        total += b
        result = result + f"{b} + "
    result = result + f"= {total}"
    return result


print(fibonacci_sequence(21))
