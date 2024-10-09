
import sys


class Employee:
    def getGivenName(self):
        return self._given
    def setGivenName(self, value):
        self._given = value

    def getFamilyName(self):
        return self._family
    def setFamilyName(self, value):
        self._family = value

    def getDateOfBirth(self):
        return self._birth
    def setDateOfBirth(self, value):
        self._birth = value


def properties(**kwargs):
    c_frame = sys._getframe(1)
    def getter(v):
        return lambda self: getattr(self.e, f'get{v}')()

    def setter(v):
        return lambda self, val: getattr(self.e, f'set{v}')(val)

    for k, v in kwargs.items():
        c_frame.f_locals[k] = property(getter(v), setter(v))

        # lambda and functions in Python performs
        # late binding in closures, so the hack "v=v"
        # is so that the proper value of "v" is replaced
        # inside the closure.
        # https://discuss.python.org/t/make-lambdas-proper-closures/10553/26

        # c_frame.f_locals[k] = property(
        #     lambda self, v=v: getattr(self.e, f'get{v}')(),
        #     lambda self, val, v=v: getattr(self.e, f'set{v}')(val)
        # )


class PyEmployee:
    def __init__(self, **kwargs):
        self.e = Employee()
        for k, v in kwargs.items():
            setattr(self, k, v)

    properties(
        given = "GivenName",
        family = "FamilyName",
        birth = "DateOfBirth",
    )


if __name__ == "__main__":
    e = PyEmployee(given="Don", family="Quixote", birth="12-11-20")
    print(e.given, e.e.getGivenName())

    e.birth = "12-03-2000"
    print(e.birth, e.e.getDateOfBirth())

