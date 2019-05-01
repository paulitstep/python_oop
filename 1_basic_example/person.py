from classtools import AttrDisplay


class Person(AttrDisplay):
    """
    Creates and maintains records that contain information about people.
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    """
    A version of the Person class adapted to match
    with special requirements.
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    joey = Person('Joey Tribbiani')
    rachel = Person('Rachel Green', job='waitress', pay=1500)
    print(joey)
    print(rachel)
    print(joey.lastName(), rachel.lastName())
    rachel.giveRaise(.10)
    print(rachel)
    chandler = Manager('Chandler Bing', 50000)
    chandler.giveRaise(.10)
    print(chandler.lastName())
    print(chandler)
