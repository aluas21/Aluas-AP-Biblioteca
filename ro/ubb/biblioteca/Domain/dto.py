from dataclasses import dataclass


@dataclass
class Customer_books:
    id_customer : int
    name_customer : int
    nr_books : int

    def __str__(self):
        return "Id customer: " + str(self.id_customer) + " name: " + str(self.name_customer) + " nr books: " + str(self.nr_books)