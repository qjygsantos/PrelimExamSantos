import unittest

def checkName(x):
    return x == 'MIGUEL'
    
class myTest(unittest.TestCase):
    def test(self):
        name = 'MIGUEL'
        self.assertTrue(checkName(name))
        
if __name__ == '__main__':
    unittest.main()
