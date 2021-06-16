from katai import *
import unittest



class Tdd(unittest.TestCase):

    def setUp(self):
        pass

    def test1_conversion(self):
        self.assertEqual(rgb_to_hex(42, 87, 235),'#2a57eb')

    def test2_conversion(self):
        self.assertNotEqual(rgb_to_hex(42, 87, 205),'#2a57eb')

    def test3_prueba_de_valores(self):
        self.assertRaises(ValueError,rgb_to_hex,-42, 87, 255)

    def test4_prueba_de_cantidad_de_valore(self):
        self.assertRaises(TypeError,rgb_to_hex,42, 87, 255, 5)
        self.assertRaises(TypeError,rgb_to_hex,42, 87)
        self.assertRaises(TypeError,rgb_to_hex, 5)



if __name__ == '__main__':
    unittest.main()
