import unittest
import task50

class Test50(unittest.TestCase):
    def test(self):
        self.assertEqual(task50.unicode("Hello world"), [72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100])


if __name__ == '__main__':
    unittest.main()