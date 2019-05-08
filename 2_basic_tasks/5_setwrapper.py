
class Set:
    def __init__(self, value=[]):
        self.data = []
        self.concat(value)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def intersection(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def difference(self, other):
        res = []
        for x in self.data:
            for y in other:
                if not x in other:
                    res.append(x)
                if not y in self.data:
                    res.append(y)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __and__(self, other):
        return self.intersection(other)

    def __xor__(self, other):
        return self.difference(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set:' + repr(self.data)


class MultiSet(Set):
    def intersection(self, *others):
        res = []
        for x in self:
            for other in others:
                if x in other:
                    res.append(x)
        return Set(res)

    def union(*args):
        res = []
        for seq in args:
            for x in seq:
                if not x in res:
                    res.append(x)
        return Set(res)


if __name__ == '__main__':
    x = Set([1, 2, 3, 4])
    y = Set([3, 4, 5])
    print(x & y)
    print(x | y)
    print(x ^ y)
    z = Set('hello')
    print(z[0], z[-1])
    for c in z:
        print(c)
    print(len(z), z)
    print(z & 'mello', z | 'mello')

    x = MultiSet([1, 2, 3, 4])
    y = MultiSet([3, 4, 5])
    z = MultiSet([0, 1, 2])
    print(x & y)
    print(x | y)
    print(x ^ y)
    print(x.intersection(y, z))
    print(x.union(y, z))
    print(x.intersection([1, 2, 3], [2, 3, 4], [1, 2, 3]))
    print(x.union(range(10)))
