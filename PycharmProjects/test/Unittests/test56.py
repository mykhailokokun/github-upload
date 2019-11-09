import unittest
import task56

class Test56(unittest.TestCase):
    def test_add(self):
        self.assertEqual(task56.add(5, 6), 11)
    def test_sub(self):
        self.assertEqual(task56.sub(10, 5), 5)
    def test_mul(self):
        self.assertEqual(task56.mul(2, 5), 10)
    def test_div(self):
        self.assertEqual(task56.div(27, 3), 9)


if __name__ == '__main__':
    unittest.main()