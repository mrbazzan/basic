
class Base:
    def __init__(self, cls, fields):
        """Every object has a class"""
        self.cls = cls
        self._fields = fields

    def _read_dict(self, field_name):
        return self._fields.get(field_name, MISSING)

    def _write_dict(self, field_name, value):
        self._fields[field_name] = value

    def read_attr(self, field_name):
        return self._read_dict(field_name)

    def write_attr(self, field_name, value):
        self._write_dict(field_name, value)


MISSING = object()

class Instance(Base):
    def __init__(self, cls):
        assert isinstance(cls, Class)  # TODO: check this!
        Base.__init__(self, cls, {})

class Class(Base):
    def __init__(self, name, base_class, fields, metaclass):
        Base.__init__(self, metaclass, fields)
        self.name = name
        self.base_class = base_class


# Base class for all objects
OBJECT = Class(name="object", base_class=None, fields={}, metaclass=None)

TYPE = Class(name="type", base_class=OBJECT, fields={}, metaclass=None)

# Everything is an instance of TYPE
TYPE.cls = TYPE
OBJECT.cls = TYPE

