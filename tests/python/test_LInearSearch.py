import sys
import os
import unittest

# Ensure the correct directory is included in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../python')))

from LinearSearch import linear_search # type: ignore

class TestLinearSearch(unittest.TestCase):
    def test_found(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)
    
    def test_not_found(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 6), -1)
    
    def test_empty_array(self):
        self.assertEqual(linear_search([], 1), -1)
    
    def test_single_element_found(self):
        self.assertEqual(linear_search([1], 1), 0)
    
    def test_single_element_not_found(self):
        self.assertEqual(linear_search([1], 2), -1)

if __name__ == '__main__':
    unittest.main()
