import unittest
from unittest import TestCase

from ro.ubb.biblioteca.Domain.D_imprumut import Imprumut
from ro.ubb.biblioteca.Repository.File_repo_books import File_repository_books
from ro.ubb.biblioteca.Repository.File_repo_customers import File_repository_customers
from ro.ubb.biblioteca.Repository.File_repo_imprumuturi import File_repository_imprumuturi
from ro.ubb.biblioteca.Service.Imprumut_service import Imprumut_service


class TestImprumut_service(TestCase):
    def setUp(self) -> None:
        self.customer_repo = File_repository_customers("../../../data/customers_test.txt")
        self.book_repo = File_repository_books("../../../data/books_test.txt")
        self.imprumut_repo = File_repository_imprumuturi("../../../data/imprumuturi_test.txt")
        self.imprumut_service = Imprumut_service(self.imprumut_repo,self.customer_repo,self.book_repo)
        self.s1 = Imprumut(1,1,1,True)
        with open("../../../data/books_test.txt", "w"):
            pass
        with open("../../../data/customers_test.txt", 'w'):
            pass
        with open("../../../data/imprumuturi_test.txt", 'w'):
            pass

    def test_add_imprumut(self):
        self.assertEqual(self.imprumut_service.get_All_imprumuturi(), [])
        self.imprumut_service.add_imprumut(1,1,1)
        self.assertEqual(len(self.imprumut_service.get_All_imprumuturi()), 1)

    def test_find_imprumut(self):
        imprumut = Imprumut(2, 1, 1, True)
        self.imprumut_service.add_imprumut(2,1,1)
        self.assertEqual(self.imprumut_service.find_imprumut(2), imprumut)

    def test_get_all_imprumuturi(self):
        self.assertEqual(self.imprumut_service.get_All_imprumuturi(), [])
        self.imprumut_repo.add_entity(self.s1)
        self.assertEqual(self.imprumut_service.find_imprumut(self.s1.id), self.s1)

    def tearDown(self) -> None:
        with open("../../../data/books_test.txt", "w"):
            pass
        with open("../../../data/customers_test.txt", 'w'):
            pass
        with open("../../../data/imprumuturi_test.txt", 'w'):
            pass

if __name__ == '__main__':
    unittest.main()
