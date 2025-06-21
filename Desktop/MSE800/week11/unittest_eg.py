#A test assertion that checks whether the output equals the expected value.


#def test_add(self):
#This method checks the add() function with 2 test cases:
#add(2, 3) should return 5
#add(-1, 1) should return 0


#If the result is not equal, the test fails and shows an error.
#A test method. All test methods must start with test_ so the test runner recognizes them.

import unittest


#Defines a function add(a, b)
def add(a, b):
    return a + b

#Defines a test class with one method test_add()
class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

#Runs tests using unittest.main()
if __name__ == '__main__':
    unittest.main()
