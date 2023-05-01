import unittest
from unittest import TestCase

from ro.ubb.biblioteca.Domain.D_entities import Customer
from ro.ubb.biblioteca.Repository.Repository_generic import Repository


class TestRepository(TestCase):
    def setUp(self) -> None:
        self.e1 = Customer(0, "Stefania Beldean", 444)
        self.e2 = Customer(1, "Alex Trifan", 555)
        self.e3 = Customer(2, "Alin Aluas", 666)
        self.repo = Repository()

    def test_get_all(self):
        self.repo.add_entity(self.e1)
        self.repo.add_entity(self.e2)
        self.repo.add_entity(self.e3)
        list = [self.e1, self.e2, self.e3]
        self.assertEqual(len(self.repo.get_all()),3)
        self.assertEqual(self.repo.get_all(),list)

    def test_get_by_id(self):
        self.repo.add_entity(self.e1)
        self.repo.add_entity(self.e2)
        self.repo.add_entity(self.e3)
        self.assertEqual(self.repo.get_by_id(1), self.e2)
        self.assertNotEqual(self.repo.get_by_id(1), self.e1)

    def test_add_entity(self):
        self.repo = Repository()
        self.repo.add_entity(self.e1)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(self.repo.get_by_id(0), self.e1)

    def test_delete_entity(self):
        self.repo.add_entity(self.e1)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(self.repo.get_by_id(0), self.e1)
        self.repo.delete_entity(self.e1.id)
        self.assertEqual(len(self.repo.get_all()), 0)
        self.assertRaises(TypeError, self.repo.get_by_id(0))

    def test_modify_entity(self):
        self.repo.add_entity(self.e1)
        self.e2 = Customer(0, "Als", 324)
        self.assertEqual(self.repo.modify_entity(self.e2), None)
        self.assertEqual(self.repo.get_by_id(0), self.e2)
        self.assertRaises(TypeError, self.repo.get_by_id(1))
        self.assertNotEqual(self.repo.get_by_id(0), self.e1)

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()