
class Customer:
    """
    >>> abass = Customer('Abass', "abass@abass.com")
    >>> abass.name
    'Abass'

    >>> x = Customer('Abass', 99)
    Traceback (most recent call last):
    ...
    TypeError: 'email' must be of type 'str'
    """
    def __init__(self, name, email, fidelity=0):
        self.name = name
        self.email = email
        self.fidelity = fidelity

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("'email' must be of type 'str'")
        elif len(value) == 0:
            raise ValueError("'email' must not be empty")
        self.__email = value

    def full_email(self):
        return f"{self.name} <{self.email}>"

