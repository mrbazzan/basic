
import unittest
from klass import Class, Instance, OBJECT, TYPE

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
