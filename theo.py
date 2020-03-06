import unittest
import CMD

class TestCMD(unittest.TestCase):
    print("performing unittest")
    def test_add(self):
        self.assertEqual(CMD.add(10,5),15)
        self.assertEqual(CMD.add(12,-5),7)
        self.assertEqual(CMD.add(-54, 5), -49)
        self.assertEqual(CMD.add(-4,-5),-9)

    def test_sub(self):
        self.assertEqual(CMD.sub(10,5),5)
        self.assertEqual(CMD.sub(12,-5),17)
        self.assertEqual(CMD.sub(-54, 5),-59)
        self.assertEqual(CMD.sub(-4,-5),1)

    def test_mul(self):
        self.assertEqual(CMD.mul(10,5),50)
        self.assertEqual(CMD.mul(12,-5),-60)
        self.assertEqual(CMD.mul(-54, 5),-270)
        self.assertEqual(CMD.mul(-4,-5),20)

    def test_div(self):
        self.assertEqual(CMD.div(10,5),2)
        self.assertEqual(CMD.div(12,-5),-2.4)
        self.assertEqual(CMD.div(-54, 5),-10.8)
        self.assertEqual(CMD.div(-4,-5),0.8)

if __name__=='__main__':
    unittest.main()
