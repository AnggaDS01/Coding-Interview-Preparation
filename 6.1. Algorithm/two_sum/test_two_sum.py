import unittest
from two_sum import two_sum

class TestTwoSum(unittest.TestCase):

    def test_two_sum(self):
        # Test case 1: Normal case
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        
        # Test case 2: No solution case
        self.assertEqual(two_sum([1, 2, 3, 4], 10), [])
        
        # Test case 3: Multiple solutions
        self.assertEqual(two_sum([3, 2, 4, 3], 6), [1, 2])
        
        # Test case 4: Negative numbers
        self.assertEqual(two_sum([-1, -2, -3, -4], -6), [1, 3])
        
        # Test case 5: Same number used twice
        self.assertEqual(two_sum([3, 3], 6), [0, 1])
        
        # Test case 6: Empty list
        self.assertEqual(two_sum([], 5), [])
        
        # Test case 7: One element
        self.assertEqual(two_sum([5], 5), [])
        
if __name__ == '__main__':
    unittest.main()
