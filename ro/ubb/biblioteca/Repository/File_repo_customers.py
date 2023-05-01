from ro.ubb.biblioteca.Domain.D_entities import Customer
from ro.ubb.biblioteca.Repository.Repository_generic import Repository


class File_repository_customers(Repository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.load_data()

    def load_data(self):
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                array = line.split(",")
                customer = Customer(int(array[0]), array[1], int(array[2]))
                self._entities[int(array[0])] = customer

    def write(self, entity):
        with open(self.__file_name, "a") as f:
            f.write(str(entity.id) + "," + entity.name + "," + str(entity.cnp)+ "\n" )

    def add_entity(self, entity):
        super().add_entity(entity)
        self.write(entity)

    def delete_entity(self, customer):
        super().delete_entity(customer)
        with open(self.__file_name, "w") as f:
            ok = 0
            for customer2 in self._entities.values():
                if ok == 0:
                    f.write(str(customer2.id) + "," + customer2.name + "," + str(customer2.cnp))
                else:
                    f.write("\n" + str(customer2.id) + "," + customer2.name + "," + str(customer2.cnp))
                ok += 1

        self.load_data()

    def modify_entity(self, customer):
        super().modify_entity(customer)
        with open(self.__file_name, "w") as f:
            ok = 0
            for customer2 in self._entities.values():
                if ok == 0:
                    f.write(str(customer2.id) + "," + customer2.name + "," + str(customer2.cnp))
                else:
                    f.write(str(customer2.id) + "," + customer2.name + "," + str(customer2.cnp)+"\n" )
                ok += 1
        self.load_data()
