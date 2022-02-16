import unittest
from employee import Employee

class EmployeeTest(unittest.TestCase):
    def setUp(self):
        first_name="John"
        last_name="Doe"
        salary=150000
        self.employee=Employee(first_name,last_name,salary)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 155000)

    def test_give_custom_raise(self):
        self.employee.give_raise(15000)
        self.assertEqual(self.employee.salary, 165000)

if __name__=='__main__':
    unittest.main()