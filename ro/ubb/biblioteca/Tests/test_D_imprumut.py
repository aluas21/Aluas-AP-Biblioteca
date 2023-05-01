import unittest
from unittest import TestCase

from ro.ubb.biblioteca.Domain.D_imprumut import Imprumut


class TestImprumut(TestCase):
    def setUp(self) -> None:
        self.imprumut = Imprumut(1,2,3,True)

    def test_id(self):
        self.assertEqual(self.imprumut.id, 1)

    def test_set_id(self):
        self.imprumut.set_id(2)
        self.assertEqual(self.imprumut.id, 2)

    def test_id_customer(self):
        self.assertEqual(self.imprumut.id_customer, 2)

    def test_id_book(self):
        self.assertEqual(self.imprumut.id_book, 3)

if __name__ == '__main__':
    unittest.main()