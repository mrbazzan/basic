
import sys


from employee import Employee


def properties(**kwargs):
    c_frame = sys._getframe(1)

    # Create getter/setter property for the keys
    # by adding it in the frame object's :f_locals: attribute.
    for k, v in kwargs.items():
        c_frame.f_locals[k] = property(
            eval(f"lambda self: self.e.get{v}()"),
            eval(f"lambda self, v: self.e.set{v}(v)"),
        )


class PyEmployee:
    def __init__(self, **kwargs):
        self.e = Employee()
        for k, v in kwargs.items():
            setattr(self, k, v)

    properties(
        given = "GivenName",
        family = "FamilyName",
        birth = "DateOfBirth"
    )


if __name__ == "__main__":
    e = PyEmployee(given="Don", family="Quixote", birth="12-11-20")
    print(e.given, e.e.getGivenName())

    e.given = "Chidera"
    print(e.given, e.e.getGivenName())

