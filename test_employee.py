"""Testing the Employee Module"""
# CHECK OUT PYTEST- ALSO UNIT TESTING
import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Testing the Employee Module"""

    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    # Will run its code before every single test
    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Leroy", "Petersen", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)

    # Will run its code after every single test
    def tearDown(self):
        print("tearDown\n")

    def test_email(self):
        """Testing Email Returned"""
        print("test_email")
        self.assertEqual(self.emp_1.email, "Leroy.Petersen@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Petersen@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        """Testing Fullname Returned"""
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Leroy Petersen")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Petersen")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        """Testing Raise Returned"""
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    # Testing mock visit to website
    def test_monthly_schedule(self):
        """Testing Website Visit as mock"""
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Petersen/May")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Smith/June")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == "__main__":
    unittest.main()
