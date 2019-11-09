def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


operation = input("Operation ")
a = int(input("1-st number"))
b = int(input("2-nd number"))

if operation == "+":
    print(add(a, b))
elif operation == "-":
    print(sub(a, b))
elif operation == "*":
    print(mul(a, b))
elif operation == "/":
    if b == 0:
        print("Na nol' delit nel'zya")
    else:
        print(div(a, b))
