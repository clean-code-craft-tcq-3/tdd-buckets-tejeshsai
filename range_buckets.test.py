import unittest
import range_buckets


class RangeBucketTest(unittest.TestCase):
    def test_range_details(self):
        self.assertTrue(range_buckets.getRangeDetails([4, 5]) == 1)
        self.assertTrue(range_buckets.getRangeDetails([2, 3, 4, 6, 7]) == 2)
        self.assertTrue(range_buckets.getRangeDetails([1, 7, 2, 3, 4, 6]) == 2)

    def test_print_range_details(self):
        self.assertTrue(range_buckets.printRangeDetails([4, 5]) == 1)
        self.assertTrue(range_buckets.printRangeDetails(
            [7, 9, 8, 4, 3, 2]) == 2)


if __name__ == '__main__':
    unittest.main()
