
# Entry point --> type.__call__(cls)

class __printer__(type):
    def __new__(meta, cls, bases, class_dict):
        print('Name            Type                 Value')
        print('-------------   ------------------   ---------------------------')
        for k, v in class_dict.items():
            print('%-15s %-20s %r' % (k, type(v), v))

        return type.__new__(meta, cls, bases, class_dict)


class Test(metaclass=__printer__):
    a = 47
    b = "raspberry"
    def c(self): pass
    d = property(lambda self: None)

