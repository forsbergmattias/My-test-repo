import unittest

class MyStingTestClass(unittest.TestCase):

    def test_upper(self): 
        self.assertEqual('foo'.upper(), 'FOO')

    def test_mybranch(self):
        self.assertEqual('foo'.lower(), 'foo')

if __name__=="__main__":
    unittest.main()