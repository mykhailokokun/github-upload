def unicode(a):
    b = []
    for i in a:
        b.append(ord(i))

    return b


a = "Hello world"
print(unicode(a))
