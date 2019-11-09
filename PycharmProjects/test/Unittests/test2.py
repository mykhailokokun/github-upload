import unittest
import task2

class Test2(unittest.TestCase):
    def test(self):
        self.assertEqual(task2.factorial(5), 120)




if __name__ == '__main__':
    unittest.main()