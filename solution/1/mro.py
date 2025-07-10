
# C3 ALGORITHM

def merge(seqs):
    pass

def mro(k):
    def inner(klass):
        b = []
        for k in klass:
            b += [[k] + inner(k.__bases__)]
        return b

    return merge([[k]] + inner(k.__bases__) + [list(k.__bases__)])

class Example:
    class D: pass
    class E: pass
    class F: pass
    class B(D,E): pass
    class C(D,F): pass
    class A(B,C): pass


import pprint; pprint.pprint(mro(Example.C))
