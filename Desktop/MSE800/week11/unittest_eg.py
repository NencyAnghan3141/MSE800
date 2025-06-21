import unittest

# Function to be tested
def add(a, b):
    return a + b

# Test class
class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

# Run tests
if __name__ == '__main__':
    unittest.main()
