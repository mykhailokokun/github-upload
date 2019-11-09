import unittest
import task14

class Test14(unittest.TestCase):
    def test(self):
        self.assertEqual(task14.string_test("Hello world"),('Upper case characters : 1', 'Lower case Characters : 9'))


if __name__ == '__main__':
    unittest.main()