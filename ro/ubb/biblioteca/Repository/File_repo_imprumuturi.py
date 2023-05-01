from ro.ubb.biblioteca.Domain.D_entities import Customer
from ro.ubb.biblioteca.Domain.D_imprumut import Imprumut
from ro.ubb.biblioteca.Repository.Repository_generic import Repository


class File_repository_imprumuturi(Repository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.load_data()

    def load_data(self):
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                array = line.split(",")
                imprumut = Imprumut(int(array[0]), int(array[1]), int(array[2]), True)
                self._entities[int(array[0])] = imprumut

    def write(self, imprumut):
        with open(self.__file_name, "a") as f:
            f.write("\n" + str(imprumut.id) + "," + str(imprumut.id_customer) + "," + str(imprumut.id_book))

    def add_entity(self, entity):
        super().add_entity(entity)
        self.write(entity)

    def delete_entity(self, imprumut):
        super().delete_entity(imprumut)
        with open(self.__file_name, "w") as f:
            ok = 0
            for imprumut2 in self._entities.values():
                if ok == 0:
                    f.write(str(imprumut2.id) + "," + str(imprumut2.id_customer) + "," + str(imprumut2.id_book))
                else:
                    f.write("\n" + str(imprumut2.id) + "," + str(imprumut2.id_customer) + "," + str(imprumut2.id_book))
                ok += 1

        self.load_data()

