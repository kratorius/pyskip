#!/usr/bin/env python
import sys
from skip import SkipDict

try:
    import unittest2 as unittest
except ImportError:
    assert(sys.version_info >= (2, 7))
    import unittest


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.skip = SkipDict()

    def test_insert(self):
        "Test insert of new elements"
        self.skip["hello"] = "world"
        self.assertEqual(self.skip["hello"], "world")

        self.skip["buenos"] = "dias"
        self.assertEqual(self.skip["buenos"], "dias")

    def test_replace(self):
        "Check that replacement of objects works correctly"
        self.skip["key"] = "value"
        self.skip["key"] = "modified"
        self.assertEqual(self.skip["key"], "modified")


class BehaveLikeDictTest(unittest.TestCase):
    "Check that the SkipDict has the same behavior of a dictionary"

    def setUp(self):
        self.skip = SkipDict()

    def test_len(self):
        "Test len() on SkipDict"
        self.skip[0] = 0
        self.skip[1] = 1
        self.skip[2] = 2
        self.skip[3] = 3
        self.assertEqual(len(self.skip), 4)

    def test_assignment(self):
        "Check __getitem__/__setitem__ assignment (through dict['key'])"
        self.skip["key"] = "value"
        self.assertEqual(self.skip["key"], "value")

    def test_keyerror(self):
        """
        A SkipDict should raise a KeyError when requesting a Key that
        has not been added to the dictionary
        """
        with self.assertRaises(KeyError):
            self.skip["unknown"]


class SpecialMethodsTest(unittest.TestCase):
    "Test for the __magic__ methods"

    def setUp(self):
        self.skip = SkipDict()

    def test_repr(self):
        self.assertIn("<SkipDict: ", repr(self.skip))
        self.assertIn("1 levels", repr(self.skip))
        self.assertIn("0 items", repr(self.skip))

        self.skip["key"] = "value"
        self.assertIn("1 items", repr(self.skip))

        self.skip["key2"] = "value2"
        self.assertIn("2 items", repr(self.skip))