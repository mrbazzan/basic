
class NonBlank:
    count = 0

    def __init__(self):
        cls = self.__class__
        self.storage_name = f"{cls}_{cls.count}"
        cls.count += 1

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("'NonBlank' must be of type 'str'")
        elif len(value) == 0:
            raise ValueError("'NonBlank' must not be empty")
        instance.__dict__[self.storage_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)


class Customer:
    """
    >>> abass = Customer('Abass', "abass@abass.com")
    >>> abass.name
    'Abass'
    >>> abass.full_email()
    'Abass <abass@abass.com>'

    >>> x = Customer('Abass', 99)
    Traceback (most recent call last):
    ...
    TypeError: 'NonBlank' must be of type 'str'
    """

    # NB: We don't want million instances of NonBlank
    # in Customer; that is why we make it a class-level
    # machinery( the actual value is then set on the
    # instance of each Customer.)

    # It wouldn't work as instance attribute. Deep this:
    # class Ex:
    #     def __init__(name):
    #         self.name = NonBlank(name)
    #
    # >>> ex = Ex("example")
    # >>> ex.name
    # It returns an instance of NonBlank not "example"

    name = NonBlank()
    email = NonBlank()

    def __init__(self, name, email, fidelity=0):
        self.name = name
        self.email = email
        self.fidelity = fidelity

    def full_email(self):
        return f"{self.name} <{self.email}>"

