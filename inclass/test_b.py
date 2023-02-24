import unittest
from b import calc_b

class TestCalcMethods(unittest.TestCase):
    def test_calc(self):
        predict = calc_b(1, 2)

        self.assertEqual(predict, 2)

if __name__ == "__main__": # __name__ 為被import進來的函數
    unittest.main()