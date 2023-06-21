import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc=Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 6, 5) == 30

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 30, 2) == 15

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 15, 5) == 10

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 10, 2) == 12