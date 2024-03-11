x = 5


def set_x(num):
    x = num
    print(x)
    return 1


def set_global_x(num):
    global x
    print(x)

    x = num
    print(x)
    return 0


print(set_x(5))

print(set_global_x(10))
