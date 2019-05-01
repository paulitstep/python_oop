
class AttrDisplay:
    """
    Implements an inherited output operation overload method that displays
    instance class names and all attributes as name=value pairs,
    available in instances (excluding attributes inherited from classes).
    Can be added to any classes and is able to work with any
    instances.
    """

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('{}={}'.format(key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__(self):
        return '[{}: {}]'.format(self.__class__.__name__, self.gatherAttrs())


if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

        def gatherAttrs(self):
            return 'Spam'

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)
