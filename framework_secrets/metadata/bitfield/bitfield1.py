
ENABLED, SIMPLE, SUNKEN, RAISED, TRANSPARENT = 1, 2, 4, 8, 16


class __bitproperties__(type):
    def __new__(meta, classname, bases, class_dict):
        for option in class_dict['bit_properties']:
            def get_property(enum):
                return property(
                    lambda self: bool(self.style & enum),
                    lambda self, v: setattr(self, 'style',
                        self.style | enum if v else
                        self.style ^ enum
                    )
                )
            enum = eval(option.upper())  # executes in the context of locals and globals
            class_dict[option] = get_property(enum)
        return super().__new__(meta, classname, bases, class_dict)


class Widget(metaclass=__bitproperties__):
    style = 0
    bit_properties = ['enabled', 'simple', 'sunken', 'raised', 'transparent']


w = Widget()
w.enabled = True
print(w.style)

w.sunken = True
print(w.style)

w.transparent = True
print(w.style)

w.sunken = False
print(w.style)

