import unittest
import random
import testclass



class testRandint(unittest.TestCase):

    def setUp(self):
        global random
        random = Random(23)

    def test_getnumber(self):
        result = testclass.getnumber(15,17)
        a = 16 
        self.assertEqual(result, a)

    def test_length(self):
        result = testclass.length(0,5)
        self.assertEqual(result,5)    

    def test_numbers(self):
        result = testclass.numbers(5)
        self.assertEqual(result,True)


    def test_potentialnumbers(self):
        result = testclass.potentialnumbers(1,6)
        f = [1, 2, 3, 4, 5]
        self.assertEqual(result,f)     
          

    def setUp(self):
        testclass.initialize()

    def tearDown(self):
        testclass.cleanUp()        
        
unittest.main()


