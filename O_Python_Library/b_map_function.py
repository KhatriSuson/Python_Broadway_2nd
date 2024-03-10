def square_num(n):
    return n * n

numbers = [ 1, 3, 4, 5]

new_num = []
for number in numbers:
    new_num.append(square_num(number))
print(new_num)

num = [1, 2, 3, 4, 5]
square_num = map(lambda x: x * x, num)
print(list(square_num))






