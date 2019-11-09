class Iterator(object):

    def __init__(self, n):
        super(Iterator, self).__init__()
        self.n = n

    def divBySeven(self):
        for i in range(0, self.n):
            if i % 7 == 0:
                yield i

a = []
for num in Iterator(100).divBySeven():
    a.append(num)

print(a)