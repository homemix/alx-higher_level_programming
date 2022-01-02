#!/usr/bin/python3
"""Unittest for class Rectangle
"""
from unittest import TestCase

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(TestCase):
    """ unittest for class TestRectangle"""
    def test_inherit_base_class(self):
        """ test inherited base class TestRectangle"""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)

    def test_create_instance(self):
        """ test if it creates a new instance"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_width_height(self):
        """unittest for width and height attributes."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        with self.assertRaises(TypeError):
            Rectangle('10', 3)
            Rectangle(10, '3')
            Rectangle('10', '3')
        with self.assertRaises(ValueError):
            Rectangle(-1, 5)
            Rectangle(-1, -5)

    def test_x_y(self):
        """unittest for x and y attributes."""
        r2 = Rectangle(10, 2, 3, 4)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, '3', 4)
            Rectangle(10, 2, 3, '4')
            Rectangle(10, 2, '3', '4')
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, '4')
            Rectangle(10, 2, -1, -1)
            Rectangle(10, 2, 0, -1)
            Rectangle(10, 2, 0, 0)

    def test_area(self):
        """ unittest for area of rectangle"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        expected = '####\n####\n####\n####\n####\n####\n'
        r1 = Rectangle(4, 6)
        self.assertEqual(r1.display(), expected)

    def test_update(self):
        self.fail()

    def test_to_dictionary(self):
        self.fail()
