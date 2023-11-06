import unittest

class Calculator:
    """
    A simple calculator class that provides basic mathematical operations.
    """

    def add(self, x, y):
        """
        Add two numbers.

        :param x: The first number.
        :param y: The second number.
        :return: The sum of x and y.
        """
        return x + y
    
    def subtract(self, x, y):
        """
        Subtract two numbers.

        :param x: The first number.
        :param y: The second number.
        :return: The result of subtracting y from x.
        """
        return x - y
    
    def multiply(self, x, y):
        """
        Multiply two numbers.

        :param x: The first number.
        :param y: The second number.
        :return: The product of x and y.
        """
        return x * y
    
    def divide(self, x, y):
        """
        Divide two numbers.

        :param x: The numerator.
        :param y: The denominator.
        :return: The result of dividing x by y.
        :raises ValueError: If y is 0, a division by zero error is raised.
        """
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y

class CalculatorTest(unittest.TestCase):
    """
    A test case for the Calculator class.
    """

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(11, self.calc.add(3, 8), "The addition is wrong")

    def test_subtract(self):
        self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is wrong")

    def test_multiply(self):
        self.assertEqual(30, self.calc.multiply(5, 6), "Multiplication is wrong")

    def test_divide(self):
        self.assertEqual(3, self.calc.divide(6, 2), "Division is wrong")

if __name__ == '__main__':
    unittest.main()
    print("Sushan")
