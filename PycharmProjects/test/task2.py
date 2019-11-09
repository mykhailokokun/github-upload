def factorial(user):
    factors = []

    while user > 0:
        n = user * (user - 1)
        if user == 1:
            factors.append(1)
            break
        else:
            factors.append(user)
            user -= 1

    result = 1
    for f in factors:
        result *= f

    return result


user = int(input("Input a number: "))
print(factorial(user))
