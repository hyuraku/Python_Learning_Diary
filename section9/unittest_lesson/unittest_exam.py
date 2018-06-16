import unittest

import calculation

release_name = 'lesson'

class Caltest(unittest.TestCase):
    def setUp(self):
        print('setup')
        self.cal = calculation.Cal()

    def tearDown(self):
        print('clean up')
        del self.cal

    # @unittest.skip('skip!')
    @unittest.skipIf(release_name == 'lesson','skip!!')
    def test_add_num_and_double(self):
        # cal=calculation.Cal()
        self.assertEqual(self.cal.add_num_and_double(1,1),4)

    def test_add_num_and_double_raise(self):
        # cal=calculation.Cal()
        #例外処理にはwithステートメントを使う
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1','1')

if __name__ == "__main__":
    unittest.main()
