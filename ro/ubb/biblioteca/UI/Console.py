from ro.ubb.biblioteca.Service.Books_service import Books_service
from ro.ubb.biblioteca.Service.Customers_service import Customers_service
from ro.ubb.biblioteca.Service.Imprumut_service import Imprumut_service


class Console:
    def __init__(self, customer_service : Customers_service, book_service : Books_service, imprumut_service : Imprumut_service):
        self.__customer_service = customer_service
        self.__book_service = book_service
        self.__imprumut_service = imprumut_service

#--------PRINT-MENU--------
    def print_menu(self):
        print("1: Add")
        print("2: Delete")
        print("3: Find")
        print("4: Modify")
        print("5: Borrow book")
        print("6: Return book")
        print("7: Most borrow books")
        print("8: Customers sort by name and their borrow books")
        print("9: First 20% of most active customers ")
        print("a: Print customers list")
        print("b: Print books list")
        print("c: Print borrows list")

    def print_customers(self):
        print(*self.__customer_service.get_All_customers(), sep = '\n')

    def print_books(self):
        print(*self.__book_service.get_All_books(), sep = '\n')

    def print_imprumuturi(self):
        print(*self.__imprumut_service.get_All_imprumuturi(), sep = '\n')

#----------ADD------------
    def option_1(self):
        print("     1. Add a customer")
        print("     2. Add a book")
        option = input("   Choose an option")
        if option == '1':
            self.add_customer()
        elif option == '2':
            self.add_book()
        else:
            print("This option is not input yet, please try again!")

    def add_customer(self):
        try:
            id = int(input("    ID: "))
            name = input("  NAME: ")
            cnp = int(input("   CNP: "))
            self.__customer_service.add_customer(id, name,cnp)
        except ValueError as e:
            print(e)

    def add_book(self):
        try:
            id = int(input("     ID: "))
            title = input("     TITLE: ")
            author = input("    AUTHOR: ")
            desc = input("      DESC: ")
            self.__book_service.add_book(id,title,author,desc)
        except ValueError as e:
            print(e)

#--------DELETE-----------
    def option_2(self):
        print("     1. Delete customer")
        print("     2. Delete book")
        option = input("Choose an option")
        if option == '1':
            self.delete_customer()
        elif option == '2':
            self.delete_book()
        else:
            print("This option is not input yet, try again!")

    def delete_customer(self):
        try:
            id = int(input("    ID CUSTOMER: "))
            self.__customer_service.delete_customer(id)
        except ValueError as e:
            print(e)

    def delete_book(self):
        try:
            id = int(input("    ID BOOK:"))
            self.__book_service.delete_book(id)
        except ValueError as e:
            print(e)

#-------FIND-BY-ID-------
    def option_3(self):
        print("     1. Find customer")
        print("     2. Find book")
        option = input("Choose an option")
        if option == '1':
            self.find_customer()
        elif option == '2':
            self.find_book()
        else:
            print("This option is not input yet, try again!")

    def find_customer(self):
        try:
            id = int(input("     ID CUSTOMER:"))
            print(self.__customer_service.find_customer(id))
        except ValueError as e:
            print(e)

    def find_book(self):
        try:
            id = int(input("     ID BOOK:"))
            print(self.__book_service.find_book(id))
        except ValueError as e:
            print(e)

#---------MODIFY--------
    def option_4(self):
        print("     1. Modify customer")
        print("     2. Modify book")
        option = input("Choose an option")
        if option == '1':
            self.modify_customer()
        elif option == '2':
            self.modify_book()
        else:
            print("This option is not input yet, try again!")

    def modify_customer(self):
        try:
            id = int(input("    ID: "))
            name = input("  NAME: ")
            cnp = int(input("   CMP: "))
            self.__customer_service.modify_customer(id, name, cnp)
        except ValueError as e:
            print(e)

    def modify_book(self):
        try:
            id = int(input("     ID: "))
            title = input("     TITLE: ")
            author = input("    AUTHOR: ")
            desc = input("      DESC: ")
            self.__book_service.modify_book(id,title,author,desc)
        except ValueError as e:
            print(e)

#--------BORROW---------
    def option_5(self):
        try:
            id_imprumut = int(input("   ID borrow: "))
            id_customer = int(input("   ID customer: "))
            id_book = int(input("   ID book: "))
            self.__imprumut_service.add_imprumut(id_imprumut, id_customer, id_book)
        except ValueError as e:
            print(e)

#--------RETURN--------
    def option_6(self):
        try:
            id_customer = int(input("   Id customer: "))
            id_book = int(input("   Id book"))
            self.__imprumut_service.return_book(id_customer, id_book)
        except ValueError as e:
            print(e)

#-------TOP-BOOKS------
    def option_7(self):
        print(*self.__imprumut_service.book_max_imprumut(), sep='\n')

#--CUSTOMERS-AND-BOOKS--
    def option_8(self):
        print(*self.__imprumut_service.generare_lista_sortare(), sep='\n')

#-----TOP-CUSTOMERS-----
    def option_9(self):
        print(*self.__imprumut_service.clienti_activi(), sep='\n')

#---ADD---BOOKS---CUSTOMERS--
    def add_all(self):
        self.__customer_service.add_customer(1, "Alin", 42314565)
        self.__customer_service.add_customer(2, "Alex", 23414565)
        self.__customer_service.add_customer(3, "Maria", 546314565)
        self.__customer_service.add_customer(4, "Ionut", 43614565)
        self.__customer_service.add_customer(5, "Bianca", 34514565)
        self.__customer_service.add_customer(6, "Alin", 89414565)
        self.__customer_service.add_customer(7, "Alex", 89414565)
        self.__customer_service.add_customer(8, "Stefan", 89414565)
        self.__customer_service.add_customer(9, "Mariana", 89414565)
        self.__customer_service.add_customer(10, "Roxana", 89414565)


        self.__book_service.add_book(1, "Ion", "Liviu Rebreanu", "Roman")
        self.__book_service.add_book(2, "Moara cu norc", "Ioan Slavici", "Nuvele")
        self.__book_service.add_book(3, "Enigma Otiliei", "G Calinescu", "Roman")
        self.__imprumut_service.add_imprumut(1, 1, 1)
        self.__imprumut_service.add_imprumut(2, 2, 1)
        self.__imprumut_service.add_imprumut(3, 3, 2)
        self.__imprumut_service.add_imprumut(4, 1, 2)
        self.__imprumut_service.add_imprumut(5, 2, 2)
        self.__imprumut_service.add_imprumut(6, 1, 3)
        self.__imprumut_service.add_imprumut(7, 4, 2)
        self.__imprumut_service.add_imprumut(8, 5, 2)
        self.__imprumut_service.add_imprumut(9, 6, 2)
        self.__imprumut_service.add_imprumut(10, 4, 1)
        self.__imprumut_service.add_imprumut(11, 7, 1)
        self.__imprumut_service.add_imprumut(12, 8, 1)
        self.__imprumut_service.add_imprumut(13, 9, 1)
        self.__imprumut_service.add_imprumut(14, 10, 1)

#----------MENU---------
    def menu(self):
        #self.add_all()
        while True:
            self.print_menu()
            optiune = input("Choose your option")
            if optiune == '1':
                self.option_1()
            elif optiune == '2':
                self.option_2()
            elif optiune == '3':
                self.option_3()
            elif optiune == '4':
                self.option_4()
            elif optiune == '5':
                self.option_5()
            elif optiune == '6':
                self.option_6()
            elif optiune == '7':
                self.option_7()
            elif optiune == '8':
                self.option_8()
            elif optiune == '9':
                self.option_9()
            elif optiune == 'a':
                self.print_customers()
            elif optiune == 'b':
                self.print_books()
            elif optiune == 'c':
                self.print_imprumuturi()
            elif optiune == 'x':
                break
            else:
                print("This option is not input yet, try again!")
