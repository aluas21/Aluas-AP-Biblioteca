from ro.ubb.biblioteca.Domain.D_imprumut import Imprumut
from ro.ubb.biblioteca.Domain.dto import Customer_books
from ro.ubb.biblioteca.Repository.File_repo_books import File_repository_books
from ro.ubb.biblioteca.Repository.File_repo_customers import File_repository_customers
from ro.ubb.biblioteca.Repository.File_repo_imprumuturi import File_repository_imprumuturi
from ro.ubb.biblioteca.Repository.Repository_generic import Repository


class Imprumut_service:
    def __init__(self, imprumut_repository : File_repository_imprumuturi, customers_repostiory: File_repository_customers, books_repository: File_repository_books):
        self.__imprumuturi_repository = imprumut_repository
        self.__customers_repository = customers_repostiory
        self.__books_repository = books_repository

    def add_imprumut(self, id_imprumut, id_customer, id_book):
        imprumut = Imprumut(id_imprumut, id_customer, id_book, True)
        if self.__imprumuturi_repository.get_by_id(id_imprumut) is None:
            if self.__imprumuturi_repository.get_by_id(id_customer) is None:
                self.__imprumuturi_repository.add_entity(imprumut)
            else:
                if self.__imprumuturi_repository.get_by_id(id_book) is None:
                    self.__imprumuturi_repository.add_entity(imprumut)
                else:
                    id_imprumut2 = -1
                    for imprumut2 in self.__imprumuturi_repository.GET_ALL().values():
                        if imprumut2.id_customer == imprumut.id_customer and imprumut2.id_book == imprumut.id_book:
                            id_imprumut2 = imprumut2.id
                            break
                    if id_imprumut2 != -1:
                        self.__imprumuturi_repository.GET_ALL()[id_imprumut2] = imprumut
                        self.__imprumuturi_repository.GET_ALL()[id_imprumut2].set_id(id_imprumut2)
                    else:
                        self.__imprumuturi_repository.add_entity(imprumut)
        else:
            raise KeyError("Duplicate id!")

    def find_imprumut(self, id_imprumut):
        return self.__imprumuturi_repository.get_by_id(id_imprumut)

    def get_All_imprumuturi(self):
        return self.__imprumuturi_repository.get_all()

    def return_book(self, id_customer, id_book):
        if self.__imprumuturi_repository.get_by_id(id_customer) is None:
            raise KeyError("Acest Client nu a imprumutat carti")
        else:
            for imprumut in self.__imprumuturi_repository.GET_ALL().values():
                if imprumut.id_book == id_book and imprumut.id_customer == id_customer:
                    self.__imprumuturi_repository.GET_ALL()[imprumut.id].status = False
                    break

    def get_nr_carti_by_id(self, id_carte):
        k = 0
        for imprumut in [*self.__imprumuturi_repository.get_all()]:
            if imprumut.id_book == id_carte:
                k += 1
        return k

    def book_max_imprumut(self):
        max = 0
        lista_id_carti = []
        for carte in [*self.__books_repository.get_all()]:
            id_carte = carte.id
            nr_carte = self.get_nr_carti_by_id(carte.id)
            if nr_carte > max:
                max = nr_carte
                lista_id_carti.clear()
                lista_id_carti.append(id_carte)
            elif nr_carte == max :
                if id_carte in lista_id_carti:
                    pass
                else:
                    lista_id_carti.append(id_carte)
        return lista_id_carti

    def get_numar_carti(self, id_customer):
        k = 0
        for imprumut in [*self.__imprumuturi_repository.get_all()]:
            if imprumut.id_customer == id_customer:
                k += 1
        return k

    def generare_lista_sortare(self):
        list_sort = []
        for customer in [*self.__customers_repository.get_all()]:
            customer_books = Customer_books(customer.id, customer.name, self.get_numar_carti(customer.id))
            if customer_books.nr_books != 0:
                list_sort.append(customer_books)

        for i in range(0, len(list_sort)-1):
            for j in range(i+1, len(list_sort)):
                if list_sort[i].name_customer > list_sort[j].name_customer:
                    client_carti = list_sort[i]
                    list_sort[i] = list_sort[j]
                    list_sort[j] = client_carti
                elif list_sort[i].name_customer== list_sort[j].name_customer:
                    if list_sort[i].nr_books < list_sort[j].nr_books:
                        client_carti = list_sort[i]
                        list_sort[i] = list_sort[j]
                        list_sort[j] = client_carti
        return list_sort

    def clienti_activi(self):
        list_sort = []
        for customer in [*self.__customers_repository.get_all()]:
            customer_books = Customer_books(customer.id, customer.name, self.get_numar_carti(customer.id))
            if customer_books.nr_books != 0:
                list_sort.append(customer_books)

        for i in range(0, len(list_sort) - 1):
            for j in range(i + 1, len(list_sort)):
                if list_sort[i].nr_books < list_sort[j].nr_books:
                    client_carti = list_sort[i]
                    list_sort[i] = list_sort[j]
                    list_sort[j] = client_carti
                elif list_sort[i].nr_books == list_sort[j].nr_books:
                    if list_sort[i].name_customer > list_sort[j].name_customer:
                        client_carti = list_sort[i]
                        list_sort[i] = list_sort[j]
                        list_sort[j] = client_carti
        lungime = len(list_sort)
        lungime = int((1/5)*lungime)
        return list_sort[:lungime]
