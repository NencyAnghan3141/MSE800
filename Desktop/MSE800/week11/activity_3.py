import unittest  # Import the unittest module for unit testing

# Create a test case class that inherits from unittest.TestCase
class TestStringMethods(unittest.TestCase):

    #1. Describe what each test method is checking
    # Test if the string 'foo' becomes 'FOO' when .upper() is called
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')  # Expected output is 'FOO'

    # Test if .isupper() returns True for uppercase strings and False otherwise
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())   # 'FOO' is all uppercase → should return True
        self.assertFalse('Foo'.isupper())  # 'Foo' is not all uppercase → should return False

    # Test the split() method and also test error handling when a wrong type is used as separator
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])  # Default split on space

        # Check that s.split() raises a TypeError if separator is not a string (e.g., an integer)
        with self.assertRaises(TypeError):
            s.split(2)

# This ensures that the test cases run only if the script is executed directly
if __name__ == '__main__':
    unittest.main()  # Run all test methods in the TestStringMethods class
