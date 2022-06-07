import unittest
import range_buckets


class RangeBucketTest(unittest.TestCase):
    def test_range_details(self):
        self.assertTrue(range_buckets.getRangeDetails([4, 5]) == 1)
        self.assertTrue(range_buckets.getRangeDetails([2, 3, 4, 6, 7]) == 2)
        self.assertTrue(range_buckets.getRangeDetails([1, 7, 2, 3, 4, 6]) == 2)


if __name__ == '__main__':
    unittest.main()
