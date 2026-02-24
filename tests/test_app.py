import unittest

from app import greet


class TestGreet(unittest.TestCase):
    def test_greet_name(self) -> None:
        self.assertEqual(greet("Neo"), "Hello, Neo!")

    def test_greet_blank(self) -> None:
        self.assertEqual(greet("   "), "Hello!")
