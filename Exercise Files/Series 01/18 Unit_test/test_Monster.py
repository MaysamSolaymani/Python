import unittest
import Monster

class Testmonster(unittest.TestCase):

    def test_default(self):
        mons = Monster.monster()
        self.assertEqual(mons.point, 20)

    def test_CheckNotEqual(self):
        mon = Monster.monster()
        new_mons = Monster.monster(30)
        self.assertNotEqual(new_mons.point, mon.point)

    def test_iters(self):
        iter = Monster.monster(25)
        iter.point = 30
        self.assertNotEqual(iter.stop, iter.point)