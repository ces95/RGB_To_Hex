from katai import *
import unittest



class Tdd(unittest.TestCase):

    def Test1_conversion(self):
        self.assertEqual(rgb_to_hex(42, 87, 235),'#2a57eb')

    def Test2_conversion(self):
        self.assertNotEqual(rgb_to_hex(42, 87, 205),'#2a57eb')

    def Test3_prueba_de_valores(self):
        self.assertRaise(ValueError,rgb_to_hex,-42, 87, 255)

    def Test4_prueba_de_cantidad_de_valore(self):
        self.assertRaise(TypeError,rgb_to_hex,42, 87, 255, 5)
        self.assertRaise(TypeError,rgb_to_hex,42, 87)
        self.assertRaise(TypeError,rgb_to_hex, 5)



if __name__ == '__main__':
    unittest.main()
