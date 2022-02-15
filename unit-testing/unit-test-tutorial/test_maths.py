import unittest
import sys
import maths

class TestMaths(unittest.TestCase):

  def test_add(self):
    self.assertEqual(maths.add(10,5), 15, "Check which operator you used, it should be the + operator")
    self.assertEquals(maths.add(-1,1), 0)
    self.assertEquals(maths.add(-1,-1), -2)
  
  def test_subtract(self):
    self.assertEquals(maths.subtract(10, 5), 5)
    self.assertEquals(maths.subtract(-1, 1), -2)
    self.assertEquals(maths.subtract(-1, -1), 0)
  
  def test_multiply(self):
    self.assertEquals(maths.multiply(10, 5), 50)
    self.assertEquals(maths.multiply(-1, 1), - 1)
    self.assertEquals(maths.multiply(-1, -1), 1)
  
  def test_divide(self):
    self.assertEquals(maths.divide(10, 5), 2)
    self.assertEquals(maths.divide(-1, 1), -1)
    self.assertEquals(maths.divide(-1, -1), 1)

if __name__ == '__main__':
   log_file = 'log_file.txt'
   with open(log_file, "w") as f:
       runner = unittest.TextTestRunner(f)
       unittest.main(testRunner=runner)