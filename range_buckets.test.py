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
        self.assertTrue(range_buckets.printRangeDetails(
            [8, 9, 10, 1, 11, 2, 5, 7]) == 3)

    def test_a2d_convertion(self):
        # converts to 2,10 amps
        self.assertTrue(range_buckets.getRangesForAmpsLists([900, 4000]) == 2)
        # converts to 2,3,10 amps
        self.assertTrue(range_buckets.getRangesForAmpsLists(
            [900, 1300, 4000]) == 2)
        # converts to 2,3,4,10 amps
        self.assertTrue(range_buckets.getRangesForAmpsLists(
            [900, 1300, 1700, 4000]) == 2)
        # converts to 5,9,2,4,10,error amps
        self.assertTrue(range_buckets.getRangesForAmpsLists(
            [2300,4150, 900, 1700, 4000, 4095]) == 4)


if __name__ == '__main__':
    unittest.main()
