import unittest

import calculation

class Caltest(unittest.TestCase):
    def test_add_num_and_doubl(self):
        cal=calculation.Cal()
        self.assertEqual(cal.add_num_and_double(1,1),4)

if __name__ == "__main__":
    unittest.main()
