import unittest
import range_buckets


class RangeBucketTest(unittest.TestCase):
    def test_range_details(self):
        self.assertTrue(range_buckets.getRangeDetails([4, 5]) == 1)


if __name__ == '__main__':
    unittest.main()
