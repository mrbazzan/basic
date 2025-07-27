
#
# PROPERTY
#

class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)


class Game:
    def getx(self): return self._x
    def setx(self, val): self._x = val,
    def delx(self): del self._x
    d6 = Property(getx, setx, delx)


if __name__ == "__main__":
    print(Game.d6)  # obj is None because the attribute
                    # is accessed on the class

    Game.d6 = 5

    g = Game()
    print(g.d6)


#
# STATIC METHODS AND CLASS METHODS
#
# STATIC METHODS
#

class StaticMethod:
    def __init__(self, func):
        self.func = func
    def __get__(self, obj, objtype=None):
        return self.func

#
# CLASS METHODS
#

class ClassMethod:
    def __init__(self, func):
        self.func = func
    def __get__(self, obj, objtype=None):
        if objtype is None: objtype = type(obj)
        return lambda *args: self.func(objtype, *args)

