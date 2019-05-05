
class Adder:
    def __init__(self, start=[]):
        self.data = start

    def __add__(self, other):
        return self.data + other

    def __radd__(self, other):
        return other + self.data


class DictAdder(Adder):
    def __add__(self, y):
        new = {}
        for k in self.data.keys():
            new[k] = self.data[k]
        for k in y.keys():
            new[k] = y[k]
        return new

    def __radd__(self, y):
        new = {}
        for k in y.keys():
            new[k] = y[k]
        for k in self.data.keys():
            new[k] = self.data[k]
        return new


if __name__ == '__main__':
    x = Adder([1, 2, 3])
    print(x + [4, 5, 6])
    print([-2, -1, 0] + x)

    x = DictAdder({1: 1})
    y1 = x + {2: 2}
    y2 = {-1: -1} + x
    print(y1)
    print(y2)
