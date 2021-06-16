import unittest
from katai import *



class Tdd(unittest.TestCase):
    def setUp(self):
        pass

    def Test1_conversion(self):
        self.assertEqual(rgb_to_hex(42, 87, 235),'#2a57eb')

    def Test2_conversion(self):
        self.assertNotEqual(rgb_to_hex(42, 87, 205),'#2a57eb')

    def Test3_prueba_de_valores(self):
        self.assertRaise(ValueError,rgb_to_hex,42, 87, 205)



if __name__ == '__main__':
    unittest.main()
