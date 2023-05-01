import unittest
from unittest import TestCase

from ro.ubb.biblioteca.Domain.D_entities import Customer
from ro.ubb.biblioteca.Repository.File_repo_customers import File_repository_customers


class TestFile_repository_customers(TestCase):
    def setUp(self) -> None:
        self.s1 = Customer(0, "Stefania Beldean", 444)
        self.s2 = Customer(1, "Alex Trifan", 555)
        self.studentRepositoryTest = File_repository_customers("../../../data/customers_test.txt")
        with open("../../../data/customers_test.txt.txt", 'w'):
            pass

    def test_write(self):
        self.studentRepositoryTest.add_entity(self.s1)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 1)

    def load_data(self):
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 0)
        self.s1 = Customer(0, "Stefania Beldean", 444)
        self.studentRepositoryTest.add_entity(self.s1)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 1)
        self.studentRepositoryTest.load_data()
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 1)

    def test_add_entity(self):
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 0)
        self.studentRepositoryTest.add_entity(self.s2)

        s5 = Customer(8, "Marius",8070)
        self.studentRepositoryTest.add_entity(s5)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 2)


    def test_delete_entity(self):
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 0)
        self.studentRepositoryTest.add_entity(self.s1)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 1)
        s5 = Customer(8, "Marius",8070)
        self.studentRepositoryTest.add_entity(s5)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 2)
        self.studentRepositoryTest.delete_entity(0)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 1)

    def test_modify_entity(self):
        s1 = Customer(0, "Stefania Beldean", 444)
        self.studentRepositoryTest.add_entity(s1)
        s1.nume = "test"
        self.assertEqual(self.studentRepositoryTest.get_by_id(s1.id), s1)

    def tearDown(self) -> None:
        with open("../../../data/customers_test.txt", 'w'):
            pass

if __name__ == '__main__':
    unittest.main()
