import math  # Importing math module for power, root, and trigonometric functions
import unittest  # Importing unittest module for writing and running unit tests

# --- Calculator Functions ---

# Adds two numbers
def add(a, b): 
    return a + b

# Subtracts the second number from the first
def subtract(a, b): 
    return a - b

# Multiplies two numbers
def multiply(a, b): 
    return a * b

# Divides the first number by the second, raises an error if dividing by zero
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Raises the first number to the power of the second
def power(a, b): 
    return a ** b

# Calculates the square root of a number, raises error for negative input
def root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

# Returns the sine of an angle in degrees, rounded to 5 decimal places
def sine(deg): 
    return round(math.sin(math.radians(deg)), 5)

# Returns the cosine of an angle in degrees, rounded to 5 decimal places
def cosine(deg): 
    return round(math.cos(math.radians(deg)), 5)

# Returns the tangent of an angle in degrees, rounded to 5 decimal places
def tangent(deg): 
    return round(math.tan(math.radians(deg)), 5)

# --- Unit Tests ---

# This class tests each calculator function using the unittest framework
class TestCalculator(unittest.TestCase):

    # Test addition
    def test_add(self): 
        self.assertEqual(add(10, 5), 15)

    # Test subtraction
    def test_subtract(self): 
        self.assertEqual(subtract(10, 5), 5)

    # Test multiplication
    def test_multiply(self): 
        self.assertEqual(multiply(10, 5), 50)

    # Test division
    def test_divide(self): 
        self.assertEqual(divide(10, 5), 2)

    # Test division by zero (should raise error)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    # Test power function
    def test_power(self): 
        self.assertEqual(power(2, 3), 8)

    # Test square root
    def test_root(self): 
        self.assertEqual(root(9), 3.0)

    # Test square root of negative number (should raise error)
    def test_root_negative(self):
        with self.assertRaises(ValueError):
            root(-9)

    # Test sine function (30° → 0.5)
    def test_sine(self): 
        self.assertAlmostEqual(sine(30), 0.5, places=2)

    # Test cosine function (60° → 0.5)
    def test_cosine(self): 
        self.assertAlmostEqual(cosine(60), 0.5, places=2)

    # Test tangent function (45° → 1.0)
    def test_tangent(self): 
        self.assertAlmostEqual(tangent(45), 1.0, places=2)

# --- Run the tests if the script is executed directly ---
if __name__ == '__main__':
    unittest.main()  # Run all test cases
# This will execute the tests when the script is run directly, allowing for easy testing of the calculator functions.
# The unittest framework will automatically discover and run all methods that start with 'test_'.