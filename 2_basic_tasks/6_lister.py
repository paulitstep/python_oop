
class ListInstance:
    def __str__(self):
        return ('<Instance of {}({}), address {}: \n{}>'.format(
            self.__class__.__name__,
            self.supers(),
            id(self),
            self.attrnames()))

    def attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname {} = {}\n'.format(attr, self.__dict__[attr])
        return result

    def supers(self):
        names = []
        for super in self.__class__.__bases__:
            names.append(super.__name__)
        return ', '.join(names)


