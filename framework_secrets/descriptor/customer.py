from customer_util import NonBlank, named_fields


@named_fields
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
    TypeError: 'email' must be of type 'str'
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

