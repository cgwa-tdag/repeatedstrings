import unittest
import repeated


class TestRepeated(unittest.TestCase):
    def test_example(self):
        nans = repeated.repeated('abcac', 10)
        self.assertEqual(nans, 4)

    def test_example0(self):
        nans = repeated.repeated('aba', 10)
        self.assertEqual(nans, 7)

    def test_example1(self):
        nans = repeated.repeated('a', 1_000_000_000_000)
        self.assertEqual(nans, 1_000_000_000_000)

    def test_example_2(self):
        nans = repeated.repeated('p', 1_000_000_000)
        self.assertEqual(nans, 0)

    def test_example_3(self):
        nans = repeated.repeated('abcd', 5000)
        self.assertEqual(nans, 5000)

    def test_example_3(self):
        nans = repeated.repeated('qbcdsfwerfjqwfeoinqwoqnwf', 5_000_000)
        self.assertEqual(nans, 0)


if __name__ == "__main__":
    unittest.main()
