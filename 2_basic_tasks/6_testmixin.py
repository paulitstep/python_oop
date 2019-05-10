
from lister import ListInstance  # rename module from '6_lister.py' to 'lister.py'


class Super:
    def __init__(self):
        self.data1 = 'Python'


class Sub(Super, ListInstance):
    def __init__(self):
        super().__init__()
        self.data2 = 'Django'
        self.data3 = 'Django Rest Framework'


if __name__ == '__main__':
    x = Sub()
    print(x)

