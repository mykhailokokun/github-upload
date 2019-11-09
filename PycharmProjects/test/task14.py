def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"] += 1
        elif c.islower():
           d["LOWER_CASE"] += 1
        else:
           pass
    return "Upper case characters : {}".format(d["UPPER_CASE"]), "Lower case Characters : {}".format(d["LOWER_CASE"])

print(string_test('Hello world!'))