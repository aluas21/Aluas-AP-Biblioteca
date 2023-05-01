from ro.ubb.biblioteca.Repository.File_repo_books import File_repository_books
from ro.ubb.biblioteca.Repository.File_repo_customers import File_repository_customers
from ro.ubb.biblioteca.Repository.File_repo_imprumuturi import File_repository_imprumuturi
from ro.ubb.biblioteca.Repository.Repository_generic import Repository
from ro.ubb.biblioteca.Service.Books_service import Books_service
from ro.ubb.biblioteca.Service.Customers_service import Customers_service
from ro.ubb.biblioteca.Service.Imprumut_service import Imprumut_service
from ro.ubb.biblioteca.UI.Console import Console


def start():
    #REPOSITORY
    #-----MEMORIE------

    #customers_repository = Repository()
    #books_repository = Repository()
    #imprumut_repository = Repository()

    #------FISIER------
    customers_repository = File_repository_customers("ro/data/customers.txt")
    books_repository = File_repository_books("ro/data/books.txt")
    imprumut_repository = File_repository_imprumuturi("ro/data/imprumuturi.txt")

    #SERVICE
    customers_service = Customers_service(customers_repository)
    books_service = Books_service(books_repository)
    imprumut_service = Imprumut_service(imprumut_repository, customers_repository, books_repository)
    consola = Console(customers_service, books_service, imprumut_service)
    consola.menu()

start()


# 1,Alin,7464536576
# 2,Alex,7987867578
# 3,Alin,9987867578
# 4,Maria,6809237898
# 5,Mara,7980236983
# 6,Alex,234234235
# 7,Ioana,234235232
# 8,Darius,134234234
# 9,Maxim,234212343
# 10,Ioan,142342343