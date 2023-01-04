from asyncio.windows_events import NULL
import unittest
from Software_Metrics_Exam import absolute

class TestAbsoluteMethods(unittest.TestCase):

    def test_equal_int(self):
        self.assertEqual(absolute(-5),5)
        self.assertEqual(absolute(5),5)

    def test_not_equal_int(self):
        self.assertNotEqual(absolute(-10), -10)
        self.assertNotEqual(absolute(10), -10)

    def test_equal_float(self):
        self.assertEqual(absolute(-0.1),0.1)
        self.assertEqual(absolute(25),25)

    def test_not_equal_float(self):
        self.assertNotEqual(absolute(-2.3), -2.3)
        self.assertNotEqual(absolute(3.14), -3.14)

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
        self.assertEqual(absolute(input_null),0.0)
        self.assertNotEqual(absolute(input_null),1)

    def test_invalid_var_type(self):
        input_wrong_type=[-5,2]
        with self.assertRaises(TypeError):
            absolute(input_wrong_type)

if __name__ == '__main__':
    unittest.main(verbosity=2)
