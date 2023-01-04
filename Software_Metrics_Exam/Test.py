import unittest
from Software_Metrics_Exam import absolute

class TestAbsoluteMethods(unittest.TestCase):

    def test_does_it_work(self):
        self.assertEqual(absolute(-5),5)
        self.assertEqual(absolute(5),5)
        self.assertNotEqual(absolute(-10), -10)
        self.assertNotEqual(absolute(10), -10)

if __name__ == '__main__':
    unittest.main()
