
# This unittest module is a means of testing Python code. It is an extension of JUnit.
# By extending from the imported class TestCase, we get some 'assert' methods that will
# test a function we give to it with a given input.

            # self.assertEqual()
            # self.assertNotEqual()
            # self.assertTrue()
            # self.assertFalse()
            # self.assertIs()
            # self.assertIsNot()
            # self.assertIsInstance()
            # self.assertIsNotInstance()
import unittest
import functions

class TestFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_adder(self):
        result = functions.adder(30, 20)
        self.assertEqual(result, 50)
        print(f'Test 1 for adder completed. Result was {result}')

        result = functions.adder(10, 10)
        for i in range(10,20):
            self.assertGreater(result, i)
        
        print(f'Test 2 for adder completed. Result was {result}')

    # def test_subber(self):
    #     self.assertEqual(functions.subber(30,20),10)

    def test_make_list(self):
        self.assertEqual(functions.make_list(1,2,3),(2,3,4))

    def test_divider(self):
        self.assertRaises(ValueError, functions.divider, 10, 0)
        with self.assertRaises(ValueError):
            functions.divider(10,5)
            
if __name__ == '__main__':
    unittest.main()