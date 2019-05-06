
class MyList:
    def __init__(self, start):
        self.wrapped = start[:]
        self.wrapped = list()
        for x in start:
            self.wrapped.append(x)

    def __add__(self, other):
        return MyList(self.wrapped + other)

    def __radd__(self, other):
        return MyList(other + self.wrapped)

    def __mul__(self, time):
        return MyList(self.wrapped * time)

    def __getitem__(self, index):
        return self.wrapped[index]

    def __len__(self):
        return len(self.wrapped)

    def __getslice__(self, low, high):
        return MyList(self.wrapped[low:high])

    def append(self, x):
        return self.wrapped.append(x)

    def __getattr__(self, name):
        return getattr(self.wrapped, name)

    def __repr__(self):
        return repr(self.wrapped)


if __name__ == '__main__':
    x = MyList('Python')
    print(x)
    print(len(x))
    print(x[2])
    print(x[1:])
    print(x + ['3.x'])
    print(['C'] + x)
    print(x * 3)
    x.append('3.x')
    print(x)
    x.sort()
    print(x)
    for c in x:
        print(c, end=' ')
