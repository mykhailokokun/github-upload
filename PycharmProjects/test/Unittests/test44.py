import unittest
import task44

class Test44(unittest.TestCase):
    def test(self):
        self.assertEqual(list(map(task44.square, filter(task44.even, [1,2,3,4,5,6,7,8,9,10]))), [4, 16, 36, 64, 100])


if __name__ == '__main__':
    unittest.main()