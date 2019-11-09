import unittest
import task8

class Test8(unittest.TestCase):
    def test(self):
        self.assertEqual(task8.sortirovka(),['bag', 'hello', 'without', 'world'])




if __name__ == '__main__':
    unittest.main()