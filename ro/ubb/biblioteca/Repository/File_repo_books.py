from ro.ubb.biblioteca.Domain.D_entities import Book
from ro.ubb.biblioteca.Repository.Repository_generic import Repository


class File_repository_books(Repository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.load_data()

    def load_data(self):
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                array = line.split(",")
                book = Book(int(array[0]), array[1], array[2], array[3])
                self._entities[int(array[0])] = book

    def write(self, book):
        with open(self.__file_name, "a") as f:
            f.write("\n" + str(book.id) + "," + book.title + "," + book.author + "," + book.desc)

    def add_entity(self, entity):
        super().add_entity(entity)
        self.write(entity)

    def delete_entity(self, book):
        super().delete_entity(book)
        with open(self.__file_name, "w") as f:
            for book2 in self._entities.values():
                f.write(str(book2.id) + "," + book2.title + "," + book2.author + "," + book2.desc)

        self.load_data()

    def modify_entity(self, book):
        super().modify_entity(book)
        with open(self.__file_name, "w") as f:
            pass
        with open(self.__file_name, "w") as f:
            ok = 0
            for book2 in self._entities.values():
                if book2 != book:
                    if ok == 1:
                        ok = 0
                        f.write("\n" + str(book2.id) + "," + book2.title + "," + book2.author + "," + book2.desc)
                    else:
                        f.write(str(book2.id) + "," + book2.title + "," + book2.author + "," + book2.desc)
                else:
                    f.write(str(book2.id) + "," + book2.title + "," + book2.author + "," + book2.desc)
                    ok = 1


        self.load_data()
