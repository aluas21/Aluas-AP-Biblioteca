import unittest
from unittest import TestCase

from ro.ubb.biblioteca.Domain.D_entities import Customer, Book


class TestCustomer(TestCase):
    def setUp(self) -> None:
        self.customer = Customer(1, "Alin", 3243)

    def test_id(self):
        self.assertEqual(self.customer.id, 1)



class TestBook(TestCase):
    def setUp(self) -> None:
        self.book = Book(1,"Ion", "Liviu", "roman")

    def test_id(self):
        self.assertEqual(self.book.id, 1)

if __name__ == '__main__':
    unittest.main()

