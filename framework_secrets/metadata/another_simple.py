# THANKS TO JAMES BRADY ON STACKOVERFLOW #

print('>>> # Defining classes:')

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print("meta: creating %s %s" % (name, bases))
        return type.__new__(cls, name, bases, dct)

    def meta_meth(cls):
        print("MyMeta.meta_meth")

    __repr__ = lambda c: c.__name__

class A():
    def __init__(self):
        super(A, self).__init__()  # (2)walk the MRO chain to B
        print("A init")

    def meth(self):
        print("A.meth")

class B(metaclass=MyMeta):
    def __init__(self):
        super(B, self).__init__()  # (3)walk the MRO chain to <object>
        print("B init")

    def meth(self):
        print("B.meth")

# even without explicitly setting the metaclass,
# it uses the metaclass of first object in the MRO?
class C(A, B):  
    def __init__(self):
        print("MRO: ", C.__mro__)
        super(C, self).__init__()  # (1)walk the MRO chain to A
        print("C init")

print('>>> c_obj = C()')
c_obj = C()
print('>>> c_obj.meth()')
c_obj.meth()
print('>>> C.meta_meth()')
C.meta_meth()
print('>>> c_obj.meta_meth()')
c_obj.meta_meth()
