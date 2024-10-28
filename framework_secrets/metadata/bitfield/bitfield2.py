
ENABLED, SIMPLE, SUNKEN, RAISED, TRANSPARENT = 1, 2, 4, 8, 16

class bit_property:
    def __init__(self, enum):
        self.enum = enum


class __bitproperties__(type):
    def __new__(meta, classname, bases, class_dict):

        bitprops = (item for item  in class_dict.items()
                    if isinstance(item[1], bit_property))

        for attr, props in bitprops:
            def get_property(enum):
                def getter(self):
                    return bool(self.style & enum)
                def setter(self, v):
                    return setattr(self, 'style',
                        self.style | enum if v else
                        self.style ^ enum
                    )
                return property(getter, setter)
            class_dict[attr] = get_property(props.enum)

        return super().__new__(meta, classname, bases, class_dict)


class Widget(metaclass=__bitproperties__):
    style = 0
    enabled = bit_property(ENABLED)
    simple_border = bit_property(SIMPLE)
    sunken_border = bit_property(SUNKEN)
    raised_border = bit_property(RAISED)
    transparent_background = bit_property(TRANSPARENT)


w = Widget()
w.enabled = True
print(w.style)

w.sunken_border = True
print(w.style)

w.transparent_background = True
print(w.style)

w.sunken_border = False
print(w.style)

