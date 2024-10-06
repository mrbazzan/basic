
from employee import Employee


class PyEmployee:
    def __init__(self, **kwargs):
        self.e = Employee()
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def given(self):
        return self.e.getGivenName()

    @given.setter
    def given(self, v):
        self.e.setGivenName(v)

    # given = property(
    #     lambda self: self.e.getGivenName(),
    #     lambda self, v: self.e.setGivenName(v)
    # )
    family = property(
        lambda self: self.e.getFamilyName(),
        lambda self, v: self.e.setFamilyName(v)
    )
    birth = property(
        lambda self: self.e.getDateOfBirth(),
        lambda self, v: self.e.setDateOfBirth(v)
    )


e = PyEmployee(given="Don", family="Quixote", birth="12-11-20")
print(e.given)
print(e.e.getGivenName())

e.given = "Chidera"
print(e.given)
print(e.e.getGivenName())

