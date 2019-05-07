from mylist import MyList  # rename module from '2_mylist.py' to 'mylist.py'


class MyListSub(MyList):
    calls = 0  # initializing call counter for subclass 'MyListSub'

    def __init__(self, start):
        self.adds = 0  # initializing call counter for each instance of given subclass
        super().__init__(start)

    def __add__(self, other):
        MyListSub.calls += 1  # call counter of subclass 'MyListSub'
        self.adds += 1  # call counter of each instance
        return super().__add__(other)

    def __radd__(self, other):
        MyListSub.calls += 1  # call counter of subclass 'MyListSub'
        self.adds += 1  # call counter of each instance
        return super().__radd__(other)

    def stats(self):
        return MyListSub.calls, self.adds


if __name__ == '__main__':
    x = MyListSub('Python')
    y = MyListSub('Django')
    print(x, y)
    print(x[2])
    print(x[1:])
    print(x + ['3.x'], y + ['2.x'])
    print(x + ['2.x'])
    print(['C'] + x, ['F'] + y)
    print(x + y)
    print(x.stats())
    print(y.stats())
