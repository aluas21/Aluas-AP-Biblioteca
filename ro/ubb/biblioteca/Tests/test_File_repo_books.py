import unittest
from unittest import TestCase

from ro.ubb.biblioteca.Domain.D_entities import Book
from ro.ubb.biblioteca.Repository.File_repo_books import File_repository_books


class TestFile_repository_books(TestCase):
    def setUp(self) -> None:
        self.s1 = Book(0, "Ion", "Liviu", "roman")
        self.s2 = Book(1, "Moara", "Slavici", "nuvela")
        self.studentRepositoryTest = File_repository_books("../../../data/books_test.txt")
        with open("../../../data/books_test.txt", 'w'):
            pass

    def test_write(self):
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 0)
        self.studentRepositoryTest.add_entity(self.s1)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 1)

    def load_data(self):
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 0)
        self.s1 = Book(0, "Ion", "Liviu", "roman")
        self.studentRepositoryTest.add_entity(self.s1)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 1)
        self.studentRepositoryTest.load_data()
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 1)

    def test_add_entity(self):
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 0)
        self.studentRepositoryTest.add_entity(self.s1)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 1)

        self.studentRepositoryTest.add_entity(self.s2)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 2)

    def test_delete_entity(self):
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 0)
        self.studentRepositoryTest.add_entity(self.s1)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 1)
        self.studentRepositoryTest.add_entity(self.s2)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 2)
        self.studentRepositoryTest.delete_entity(1)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 1)
        self.studentRepositoryTest.delete_entity(0)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 0)


    def test_modify_entity(self):
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 0)
        s1 = Book(0, "Ion", "Liviu", "roman")
        self.studentRepositoryTest.add_entity(s1)
        s1.title= "test"
        self.assertEqual(self.studentRepositoryTest.get_by_id(s1.id), s1)

    def tearDown(self) -> None:
        with open("../../../data/books_test.txt", 'w'):
            pass

if __name__ == '__main__':
    unittest.main()