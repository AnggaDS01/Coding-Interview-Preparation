import unittest
from insertion_sort_algorithm import insertion_sort
from selection_sort_algorithm import selection_sort
from merge_sort_algorithm import merge_sort
from heap_sort_algorithm import heap_sort
from quick_sort_algorithm import quick_sort
from counting_sort_algorithm import counting_sort
from radix_sort_algorithm import radix_sort
from bubble_sort_algorithm import bubble_sort

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        # Data untuk testing
        self.test_cases = [
            ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
            ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
            ([3, 0, 2, 5, -1, 4, 1], [-1, 0, 1, 2, 3, 4, 5]),
            # ([], []),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([2, 1], [1, 2]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([3, 2, 1, 4], [1, 2, 3, 4]),
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([4, 3, 2, 1, 5], [1, 2, 3, 4, 5]),
            # ([1.2, 1.1, 1.3], [1.1, 1.2, 1.3]),
        ]

    def test_insertion_sort(self):
        for unsorted_arr, sorted_arr in self.test_cases:
            self.assertEqual(insertion_sort(unsorted_arr[:]), sorted_arr)

    def test_selection_sort(self):
        for unsorted_arr, sorted_arr in self.test_cases:
            self.assertEqual(selection_sort(unsorted_arr[:]), sorted_arr)

    def test_merge_sort(self):
        for unsorted_arr, sorted_arr in self.test_cases:
            self.assertEqual(merge_sort(unsorted_arr[:]), sorted_arr)

    def test_heap_sort(self):
        for unsorted_arr, sorted_arr in self.test_cases:
            self.assertEqual(heap_sort(unsorted_arr[:]), sorted_arr)

    def test_quick_sort(self):
        for unsorted_arr, sorted_arr in self.test_cases:
            self.assertEqual(quick_sort(unsorted_arr[:], 0, len(unsorted_arr) - 1), sorted_arr)

    def test_counting_sort(self):
        for unsorted_arr, sorted_arr in self.test_cases:
            if all(i >= 0 for i in unsorted_arr):  # Counting sort only works for non-negative numbers
                self.assertEqual(counting_sort(unsorted_arr[:]), sorted_arr)

    def test_radix_sort(self):
        for unsorted_arr, sorted_arr in self.test_cases:
            if all(i >= 0 for i in unsorted_arr):  # Radix sort only works for non-negative numbers
                self.assertEqual(radix_sort(unsorted_arr[:]), sorted_arr)

    def test_bubble_sort(self):
         for unsorted_arr, sorted_arr in self.test_cases:
            self.assertEqual(bubble_sort(unsorted_arr[:]), sorted_arr)

if __name__ == "__main__":
    unittest.main()
