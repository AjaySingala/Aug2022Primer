import unittest
import examplesToTest
from examplesToTest import sentence, surface_area_cube, registration

class testExamples(unittest.TestCase):
    def test_sentence(self):
        testCase = ['Akiem', 'carwash', 1800]
        self.assertEqual(sentence(testCase[0], testCase[1], testCase[2]), 'Akiem will go to the carwash at 1800.')
        testCase2 = ['Bob', 'wehadababyitsaboy', '1800']
        self.assertEqual(sentence(testCase2[0], testCase2[1], testCase2[2]), 'Bob will go to the wehadababyitsaboy at 1800.')

    def test_SurfaceAreaCube(self):
        testCase = [7,6,5]
        self.assertEqual(surface_area_cube(testCase[0], testCase[1], testCase[2]), 214)
        self.assertIs(type(surface_area_cube(testCase[0], testCase[1], testCase[2])), int)

    def test_registration(self):
        testCase = ['name', 34]
        self.assertIs(type(registration("Akiem", 13)), str)

if __name__ == '__main__':
    unittest.main()