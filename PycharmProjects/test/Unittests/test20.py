import unittest
import task20

class Test20(unittest.TestCase):
    def test(self):
        c = task20.Iterator(100)
        res = list(c.divBySeven())
        self.assertEqual(res, [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98])

if __name__ == '__main__':
    unittest.main()