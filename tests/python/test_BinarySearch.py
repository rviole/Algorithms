import sys
import os
import unittest

# Ensure the correct directory is included in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../python')))

from BinarySearch import binary_search, binary_search_recursive # type: ignore

class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5], 3), 2)
    
    def test_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), None)
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5], 6), None)
    
    def test_empty_array(self):
        self.assertEqual(binary_search([], 1), None)
        self.assertEqual(binary_search_recursive([], 1), None)
    
    def test_single_element_found(self):
        self.assertEqual(binary_search([1], 1), 0)
        self.assertEqual(binary_search_recursive([1], 1), 0)
    
    def test_single_element_not_found(self):
        self.assertEqual(binary_search([1], 2), None)
        self.assertEqual(binary_search_recursive([1], 2), None)

if __name__ == '__main__':
    unittest.main()
