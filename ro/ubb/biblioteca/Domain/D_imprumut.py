from dataclasses import dataclass


@dataclass
class Imprumut:
    __id_imprumut: int
    __id_customer : int
    __id_book : int
    status : bool

    @property
    def id(self):
        return self.__id_imprumut

    def set_id(self, new_id):
        self.__id_imprumut = new_id

    @property
    def id_customer(self):
        return self.__id_customer

    @property
    def id_book(self):
        return self.__id_book

    def __str__(self):
        return str(self.id) + " Id customer: " + str(self.__id_customer) + " id book: " + str(self.__id_book) + " status: " + str(self.status)