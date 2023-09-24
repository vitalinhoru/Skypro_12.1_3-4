import unittest

from utils.arrs import get, my_slice

class TestArrs(unittest.TestCase):
    def test_get(self):
        self.assertEquals(get([1, 2, 3], 1, 'test'), 2)
        self.assertEquals(get([], 0, 'test'), 'test')

    def test_my_slice(self):
        self.assertEquals(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEquals(my_slice([1, 2, 3], 1), [2, 3])
        self.assertEquals(my_slice([]), [])
        self.assertEquals(my_slice([1, 2, 3], None, 3), [1, 2, 3])