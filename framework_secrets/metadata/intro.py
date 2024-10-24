
# METAPROGRAMMING
# Every class has a "class" from which it is
# created from except "type".
# This means that every class is an instance of something
# Special (dunder) methods are called on a class' class


class quick(type):
    def __new__(meta, cls, bases, class_dict):
        print("here first")
        return type.__new__(meta, 'J', bases, class_dict)


class quick_one(type, metaclass=quick):
    def __new__(meta, cls, bases, class_dict):
        print("then here")
        return type.__new__(meta, meta.__name__, bases, class_dict)

    def __call__(cls, *args, **kwargs):
        print("here")
        return super().__call__()


class Fred(metaclass=quick_one):
    def __new__(cls, *a, **kw):
        print("??")
        return super().__new__(cls, *a, **kw)

    def __call__(cls):
        print("() on instance of Fred")
        pass

F = type('Fred', (), {})
print("Is INSTANCE: ", isinstance(Fred, quick_one))
print(F.__name__, Fred.__name__)
Fred()  # here --> ??
Fred()()  # here --> ?? --> () on instance of Fred

