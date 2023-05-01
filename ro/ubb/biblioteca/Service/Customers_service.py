from ro.ubb.biblioteca.Domain.D_entities import Customer
from ro.ubb.biblioteca.Repository.File_repo_customers import File_repository_customers
from ro.ubb.biblioteca.Repository.Repository_generic import Repository


class Customers_service:
    def __init__(self, customers_repository : File_repository_customers):
        self.__customers_repository = customers_repository

    def add_customer(self, id_customer, name, cnp):
        customer = Customer(id_customer, name, cnp)
        self.__customers_repository.add_entity(customer)

    def delete_customer(self, id_customer):
        self.__customers_repository.delete_entity(id_customer)

    def modify_customer(self, id_customer, name, cnp):
        customer = Customer(id_customer, name, cnp)
        self.__customers_repository.modify_entity(customer)

    def find_customer(self, id_customer):
        return self.__customers_repository.get_by_id(id_customer)

    def get_All_customers(self):
        return self.__customers_repository.get_all()