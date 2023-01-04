from asyncio.windows_events import NULL
import unittest
from Software_Metrics_Exam import absolute

class TestAbsoluteMethods(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(absolute(-5),5)
        self.assertEqual(absolute(5),5)

    def test_not_equal(self):
        self.assertNotEqual(absolute(-10), -10)
        self.assertNotEqual(absolute(10), -10)

    def test_input_str(self):
       input_str="-5";
       with self.assertRaises(TypeError):
            absolute(input_str)

    def test_input_blank(self):
        input_blank=""
        with self.assertRaises(TypeError):
            absolute(input_blank)
    
    def test_input_null(self):
        input_null=NULL
        with self.assertRaises(TypeError):
            absolute(input_null)

    def test_invalid_var_type(self):
        input_wrong_type=[-5,2]
        with self.assertRaises(TypeError):
            absolute(input_wrong_type)

if __name__ == '__main__':
    unittest.main()
