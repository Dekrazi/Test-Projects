import unittest
import controller

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(controller.add(10, 5), 15)
        self.assertEqual(controller.add(-1, 1), 0)
        self.assertEqual(controller.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(controller.subtract(10, 5), 5)
        self.assertEqual(controller.subtract(-1, 1), -2)
        self.assertEqual(controller.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(controller.multiply(10, 5), 50)
        self.assertEqual(controller.multiply(-1, 1), -1)
        self.assertEqual(controller.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(controller.divide(10, 5), 2)
        self.assertEqual(controller.divide(-1, 1), -1)
        self.assertEqual(controller.divide(5, 2), 2.5)
        self.assertRaises(ValueError, controller.divide, 10, 0)



if __name__ == "__main__":
    unittest.main()

#terminal command: python test_calc.py