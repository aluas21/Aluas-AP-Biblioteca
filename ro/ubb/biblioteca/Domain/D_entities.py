from dataclasses import dataclass


@dataclass
class Customer:
    __id_customer : int
    name : str
    cnp : int

    @property
    def id(self):
        return self.__id_customer

    def __str__(self):
        return "Id: " + str(self.__id_customer) + " name: " + self.name + " cnp: " + str(self.cnp)

@dataclass
class Book:
    __id_book : int
    title : str
    author : str
    desc : str

    @property
    def id(self):
        return self.__id_book

    def __str__(self):
        return "Id: " + str(self.__id_book) + " title: " + self.title + " author: " + self.author + " desc: " + self.desc




