"""Creates and returns Employee Information"""
import requests


class Employee:
    """A sample Employee class."""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        """Return Employee Email Address"""
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        """Returns Employee's fullname"""
        return f"{self.first} {self.last}"

    def apply_raise(self):
        """Applies raise to Employee"""
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f"http://company.com/{self.last}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad Response!"
