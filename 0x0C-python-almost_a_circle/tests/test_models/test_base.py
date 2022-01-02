#!/usr/bin/python3
"""Unittest for class Base
"""
from unittest import TestCase
from models.base import Base


class TestBase(TestCase):
    """ unittest for class TestBase"""

    def test_has_id(self):
        """ unittest for attribute id"""
        base = Base()
        self.assertEqual(base.id, 1)

    def test_to_json_string(self):
        actual = []
        self.fail()

    def test_save_to_file(self):
        self.fail()

    def test_from_json_string(self):
        self.fail()

    def test_create(self):
        self.fail()

    def test_load_from_file(self):
        self.fail()


if __name__ == "__main__":
    unittest.main()
