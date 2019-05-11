
class Animal:
    def speak(self):
        print('Welcome!')

    def reply(self):
        return self.speak()


class Mammal(Animal):
    def speak(self):
        print('huh')


class Cat(Mammal):
    def speak(self):
        print('meow')


class Dog(Mammal):
    def speak(self):
        print('bark')


class Primate(Mammal):
    def speak(self):
        print('Hello World!')


class Hacker(Primate):
    pass


if __name__ == '__main__':
    x = Cat()
    x.speak()
    x.reply()
    y = Hacker()
    y.speak()
    y.reply()
