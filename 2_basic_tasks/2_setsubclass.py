
class Set(list):
    def __init__(self, value=[]):
        super().__init__([])
        self.concat(value)

    def concat(self, value):
        for x in value:
            if not x in self:
                self.append(x)

    def intersection(self, other):
        res = []
        for x in self:
            if x in other:
                res.append(x)
        return Set(res)

    def difference(self, other):
        res = []
        for x in self:
            for y in other:
                if not x in other:
                    res.append(x)
                if not y in self:
                    res.append(y)
        return Set(res)

    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res

    def __and__(self, other):
        return self.intersection(other)

    def __xor__(self, other):
        return self.difference(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set:' + super().__repr__()


if __name__ == '__main__':
    x = Set([1, 1, 3, 3, 5, 5, 7, 7])
    y = Set([2, 2, 1, 1, 4, 4, 5, 5, 6, 6])
    print(x)
    print(y)
    print(len(x))
    print(len(y))
    print(x.intersection(y))
    print(x & y)
    print(x.difference(y))
    print(x ^ y)
    print(y.union(x))
    print(y | x)
    x.reverse()
    print(x)
