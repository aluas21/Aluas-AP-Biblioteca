import unittest
from unittest import TestCase

from ro.ubb.biblioteca.Domain.D_entities import Customer
from ro.ubb.biblioteca.Repository.File_repo_customers import File_repository_customers
from ro.ubb.biblioteca.Service.Customers_service import Customers_service


class TestCustomers_service(TestCase):
    def setUp(self) -> None:
        self.studentRepository = File_repository_customers("../../../data/customers_test.txt")
        self.studentService = Customers_service(self.studentRepository)
        self.s1 = Customer(0, "Stefania Beldean", 46568544)
        with open("../../../data/customers_test.txt", 'w'):
            pass

    def test_add_customer(self):
        self.assertEqual(self.studentService.get_All_customers(), [])
        self.studentService.add_customer(0, "Stefania Beldean", 444)
        self.assertEqual(len(self.studentService.get_All_customers()), 1)

    def test_delete_customer(self):
        self.assertEqual(self.studentService.get_All_customers(), [])
        self.studentService.add_customer(0, "Stefania Beldean", 444)
        self.assertEqual(len(self.studentService.get_All_customers()), 1)
        self.studentService.add_customer(1, "Alin Aluas", 444)
        self.assertEqual(len(self.studentService.get_All_customers()), 2)
        self.studentService.delete_customer(1)
        self.assertEqual(len(self.studentService.get_All_customers()), 1)

    def test_modify_customer(self):
        self.assertEqual(self.studentService.get_All_customers(), [])
        self.studentService.add_customer(0, "Stefania Beldean", 444)
        self.assertEqual(len(self.studentService.get_All_customers()), 1)
        self.studentService.add_customer(1, "Alin Aluas", 444)
        self.assertEqual(len(self.studentService.get_All_customers()), 2)
        idStudent = 1
        self.studentRepository.delete_entity(idStudent)
        self.assertEqual(len(self.studentService.get_All_customers()), 1)

    def test_find_customer(self):
        idStudent = 0
        numeNou = "Alex Trifan"
        cnp = 5786786567
        self.assertEqual(self.studentService.get_All_customers(), [])
        self.studentRepository.add_entity(self.s1)
        s5 = Customer(idStudent,numeNou,cnp)
        self.assertEqual(self.studentService.get_All_customers(), [self.s1])

    def test_get_all_customers(self):
        self.assertEqual(self.studentService.get_All_customers(), [])
        self.studentRepository.add_entity(self.s1)
        self.assertEqual(self.studentService.find_customer(self.s1.id), self.s1)

    def tearDown(self) -> None:
        with open("../../../data/customers_test.txt", 'w'):
            pass

if __name__ == '__main__':
    unittest.main()