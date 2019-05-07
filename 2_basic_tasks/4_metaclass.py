
class Meta:
    def __getattr__(self, name):
        print('get', name)

    def __setattr__(self, name, value):
        print('set', name, value)


if __name__ == '__main__':
    x = Meta()
    x.append = '+'
    x.append
    x.lang = 'Python'
    x.lang
    x.framework
    x.framework = 'Django'
