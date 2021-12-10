import unittest
max_integer = __import__('6-max_integer').max_integer

"""
A unittest for functions max_integer 
"""


class TestMaxInteger(unittest.TestCase):
    """
    tests for functions max_integer
    """

    def test_max_integer(self):
        """
        use cases for the functions max_integer tests
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer, [1, 2, 3, '4'])