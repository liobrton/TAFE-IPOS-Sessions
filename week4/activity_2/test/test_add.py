import unittest
from src.add import add


class TestAdd(unittest.TestCase):
    def test_add_with_different_types(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1.0, 3.2), 4.2)
        self.assertEqual(add(3, 2-1), 4)

    def test_add_typeerror_raised(self):
        self.assertRaises(TypeError, add, ('hello', 3))
        self.assertRaises(TypeError, add, (6, 'hello'))