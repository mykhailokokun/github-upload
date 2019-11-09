import unittest
import task26

class Test26(unittest.TestCase):
    def test(self):
        self.assertEqual(task26.suma(8, 9), 17)


if __name__ == '__main__':
    unittest.main()