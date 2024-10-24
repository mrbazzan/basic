
# DIFFERENT TYPES OF CLASS MEMBERS
from inspect import isfunction, isdatadescriptor, isclass

def seperate_members(class_dict):
    d = dict(methods=[], properties=[], other=[])
    for k, v in class_dict.items():
        if isfunction(v):
            d['methods'].append(k)
        elif isdatadescriptor(v):
            d['properties'].append(k)
        elif not isclass(v):
            d['other'].append(k)
    return d


class __printer__(type):
    def __new__(meta, classname, bases, class_dict):
        mem = seperate_members(class_dict)
        for k, v in mem.items():
            print(k + ":")
            for element in v:
                print("- " + element)
            print("-"*80)
        return type.__new__(meta, classname, bases, class_dict)


class Test(metaclass=__printer__):
    a = 47
    b = 'raspberry'
    def c(self): pass
    d = property(lambda self: None)
    e = 45.67
    f = [23, 24, 25]
    g = lambda self: None
    def h(self, v): self.v = v
    i = property(c, h)

