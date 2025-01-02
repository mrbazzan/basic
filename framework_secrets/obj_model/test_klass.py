
import unittest
from klass import Class, Instance, OBJECT, TYPE

# To run:
#   python -m unittest test_klass.py

class TestObjectModel(unittest.TestCase):
    def test_read_and_write_field(self):
    
        # Normal PYTHON IMPL.
        class A:
            pass
        obj = A()
        obj.a = 1
        self.assertEqual(obj.a, 1)
    
        obj.b = 5
        self.assertEqual(obj.a, 1)
        self.assertEqual(obj.b, 5)
    
        obj.a = 2
        self.assertEqual(obj.a, 2)
        self.assertEqual(obj.b, 5)
    
        # Custom IMPL
        B = Class(name='B', base_class=OBJECT, fields={}, metaclass=TYPE)
        b_obj = Instance(B)
        b_obj.write_attr('a', 1)
        self.assertEqual(b_obj.read_attr('a'), 1)
    
        b_obj.write_attr('b', 5)
        self.assertEqual(b_obj.read_attr('a'), 1)
        self.assertEqual(b_obj.read_attr('b'), 5)
    
        b_obj.write_attr('a', 2)
        self.assertEqual(b_obj.read_attr('a'), 2)
        self.assertEqual(b_obj.read_attr('b'), 5)

    def test_read_and_write_field_class(self):
        # Normal PYTHON IMPL.
        class A:
            pass
        A.a = 1
        self.assertEqual(A.a, 1)
        A.a = 6
        self.assertEqual(A.a, 6)

        # Custom IMPL
        B = Class(name="B", base_class=OBJECT, fields={'a':1}, metaclass=TYPE)
        self.assertEqual(B.read_attr('a'), 1)
        B.write_attr('a', 6)
        self.assertEqual(B.read_attr('a'), 6)

    def test_instance(self):
        # Normal PYTHON IMPL.
        class A:
            pass
        class B(A):
            pass
        b = B()
        self.assertIsInstance(b, B)
        self.assertIsInstance(b, A)
        self.assertIsInstance(b, object)
        self.assertFalse(isinstance(b, type))

        # Custom IMPL.
        _A = Class(name='_A', base_class=OBJECT, fields={}, metaclass=TYPE)
        _B = Class(name='_B', base_class=_A, fields={}, metaclass=TYPE)
        _b = Instance(_B)
        self.assertTrue(_b.isinstance(_B))
        self.assertTrue(_b.isinstance(_A))
        self.assertTrue(_b.isinstance(OBJECT))
        self.assertFalse(_b.isinstance(TYPE))

    def test_call_method(self):
        # Normal PYTHON IMPL
        class A:
            def f(self):
                return self.x + 1
        a = A()
        a.x = 1
        self.assertEqual(a.f(), 2)

        class B(A):
            pass

        b = B()
        b.x = 1
        self.assertEqual(b.f(), 2)

        # Custom IMPL.
        def f(self):
            return self.read_attr('x') + 1
        _A = Class(name="_A", base_class=OBJECT, fields={'f': f}, metaclass=TYPE)
        _a = Instance(_A)
        _a.write_attr('x', 1)
        self.assertEqual(_a.call_method('f'), 2)

        _B = Class(name="_B", base_class=_A, fields={}, metaclass=TYPE)
        _b = Instance(_B)
        _b.write_attr('x', 1)
        self.assertEqual(_b.call_method('f'), 2)

    def test_call_method_with_subclass_and_args(self):
        # Normal PYTHON IMPL
        class A:
            def f(self, arg):
                return self.x + arg
        a = A()
        a.x = 1
        self.assertEqual(a.f(1), 2)

        class B(A):
            def f(self, arg):
                return self.x + (arg*2)

        b = B()
        b.x = 1
        self.assertEqual(b.f(2), 5)

        # Custom IMPL.
        def f_A(self, arg):
            return self.read_attr('x') + arg
        def f_B(self, arg):
            return self.read_attr('x') + (arg * 2)

        _A = Class(name="_A", base_class=OBJECT, fields={'f': f_A}, metaclass=TYPE)
        _a = Instance(_A)
        _a.write_attr('x', 1)
        self.assertEqual(_a.call_method('f', 1), 2)

        _B = Class(name="_B", base_class=_A, fields={'f': f_B}, metaclass=TYPE)
        _b = Instance(_B)
        _b.write_attr('x', 1)
        self.assertEqual(_b.call_method('f', 2), 5)
