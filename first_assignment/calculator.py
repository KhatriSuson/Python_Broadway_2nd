def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        return "Error! You can't divided by Zero."
    else:
        return x / y


print("Select Operator:")
print("+. Add")
print("-. Sub")
print("*. Mul")
print("/. Div")

while True:
    op = input("Enter operator(+, -, *, /):")

    if op in ("+", "-", "*", "/"):
        a = int(input("First number :"))
        b = int(input("Second number :"))

        if op == "+":
            print("The sum of two number =", add(a, b))

        elif op == "-":
            print("The subtraction of two number = ", sub(a, b))

        elif op == "*":
            print("The multiply of two number =", mul(a, b))

        elif op == "/":
            print("The division of two number =", div(a, b))

        else:
            print("Invalid Input Operator")
