class NonBlank:
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"'{self.storage_name}' must be of type 'str'")
        elif len(value) == 0:
            raise ValueError(f"'{self.storage_name}' must not be empty")
        instance.__dict__[self.storage_name] = value


def named_fields(cls):
    for name, attr in cls.__dict__.items():
        if isinstance(attr, NonBlank):
            attr.storage_name = name
    return cls
