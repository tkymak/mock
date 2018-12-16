import unittest
from sample import Sample
from unittest.mock import Mock


class TestSample(unittest.TestCase):

    # mockなしテスト
    def test_add_method(self):
        sample = Sample()
        self.assertEqual(sample.add_method(2, 5), 7)

    # mock化
    def test_add_method_with_mock(self):
        sample = Mock()
        sample.add_method.return_value = 100
        self.assertEqual(sample.add_method(2, 5), 100)


if __name__ == '__main__':
    unittest.main()