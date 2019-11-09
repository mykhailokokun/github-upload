import unittest
import task32

class Test32(unittest.TestCase):
    def test(self):
        self.assertEqual(task32.spisok(), ('Mykhailo'))


if __name__ == '__main__':
    unittest.main()