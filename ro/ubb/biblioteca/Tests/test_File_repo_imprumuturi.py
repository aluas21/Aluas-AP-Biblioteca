import unittest
from unittest import TestCase

from ro.ubb.biblioteca.Domain.D_imprumut import Imprumut
from ro.ubb.biblioteca.Repository.File_repo_imprumuturi import File_repository_imprumuturi


class TestFile_repository_imprumuturi(TestCase):
    def setUp(self) -> None:
        self.s1 = Imprumut(0, 1, 1, True)
        self.s2 = Imprumut(1, 2, 2, True)
        self.studentRepositoryTest = File_repository_imprumuturi("../../../data/imprumuturi_test.txt")
        with open("../../../data/imprumuturi_test.txt", 'w'):
            pass

    def test_write(self):
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 0)
        self.studentRepositoryTest.add_entity(self.s1)
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 1)

    def load_data(self):
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 0)
        self.s1 = Imprumut(0, 1, 1, True)
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
        self.studentRepositoryTest.delete_entity('1')
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 1)
        self.studentRepositoryTest.delete_entity('0')
        self.assertEqual(len(self.studentRepositoryTest.get_all()), 0)

    def tearDown(self) -> None:
        with open("../../../data/imprumuturi_test.txt", 'w'):
            pass

if __name__ == '__main__':
    unittest.main()