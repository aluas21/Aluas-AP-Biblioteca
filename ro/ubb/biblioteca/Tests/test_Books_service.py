import unittest
from unittest import TestCase

from ro.ubb.biblioteca.Domain.D_entities import Book
from ro.ubb.biblioteca.Repository.File_repo_books import File_repository_books
from ro.ubb.biblioteca.Service.Books_service import Books_service


class TestBooks_service(TestCase):
    def setUp(self) -> None:
        self.repo_books = File_repository_books("../../../data/books_test.txt")
        self.books_service = Books_service(self.repo_books)
        self.s1 = Book(0,"Moara", "Slavici", "nuvela")
        with open("../../../data/books_test.txt", "w"):
            pass

    def test_add_book(self):
        self.assertEqual(self.books_service.get_All_books(), [])
        self.books_service.add_book(0,"Moara", "Slavici", "nuvela")
        self.assertEqual(len(self.books_service.get_All_books()), 1)

    def test_delete_book(self):
        self.assertEqual(self.books_service.get_All_books(), [])
        self.books_service.add_book(0,"Moara", "Slavici", "nuvela")
        self.assertEqual(len(self.books_service.get_All_books()), 1)
        self.books_service.add_book(1,"Ion", "Liviu", "roman")
        self.assertEqual(len(self.books_service.get_All_books()), 2)
        self.books_service.delete_book(1)
        self.assertEqual(len(self.books_service.get_All_books()), 1)

    def test_modify_book(self):
        self.assertEqual(self.books_service.get_All_books(), [])
        self.books_service.add_book(0,"Moara", "Slavici", "nuvela")
        self.assertEqual(len(self.books_service.get_All_books()), 1)
        self.books_service.add_book(1,"Ion", "Liviu", "roman")
        self.assertEqual(len(self.books_service.get_All_books()), 2)
        idStudent = 1
        self.books_service.delete_book(idStudent)
        self.assertEqual(len(self.books_service.get_All_books()), 1)

    def test_find_book(self):
        idbook = 1
        title = "Ion"
        author = "Liviu"
        desc = "roman"
        self.assertEqual(self.books_service.get_All_books(), [])
        self.repo_books.add_entity(self.s1)
        s5 = Book(idbook,title,author,desc)
        self.assertEqual(self.books_service.get_All_books(), [self.s1])

    def test_get_all_books(self):
        self.assertEqual(self.books_service.get_All_books(), [])
        self.repo_books.add_entity(self.s1)
        self.assertEqual(self.books_service.find_book(self.s1.id), self.s1)

    def tearDown(self) -> None:
        with open("../../../data/books_test.txt", "w"):
            pass

if __name__ == '__main__':
    unittest.main()
