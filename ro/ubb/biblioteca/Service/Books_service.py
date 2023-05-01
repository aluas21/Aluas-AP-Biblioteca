from ro.ubb.biblioteca.Domain.D_entities import Book
from ro.ubb.biblioteca.Repository.File_repo_books import File_repository_books
from ro.ubb.biblioteca.Repository.Repository_generic import Repository


class Books_service:

    def __init__(self, book_repository : File_repository_books):
        self.__book_repository = book_repository

    def add_book(self, id_book, title, author, desc):
        book = Book(id_book, title, author, desc)
        self.__book_repository.add_entity(book)

    def delete_book(self, id_book):
        self.__book_repository.delete_entity(id_book)

    def modify_book(self, id_book, title, author, desc):
        book = Book(id_book, title, author, desc)
        self.__book_repository.modify_entity(book)

    def find_book(self, id_book):
        return self.__book_repository.get_by_id(id_book)

    def get_All_books(self):
        return self.__book_repository.get_all()