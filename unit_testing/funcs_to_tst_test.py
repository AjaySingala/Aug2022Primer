# funcs_to_tst_test.py

import unittest
import funcs_to_tst

class TestFunctions(unittest.TestCase):
    def setUp(self):
        # initialize here.
        pass

    def test_sentence_returns_message(self):
        # Arrange.
        name = "John"
        place = "Boston"
        time = "12 noon"
        expected = f'{name} will go to the {place} at {time}.'

        # Act.
        result = funcs_to_tst.sentence(name, place, time)

        # Assert.
        self.assertEqual(result, expected)

    def test_sentence_check_wrong_message(self):
        # Arrange.
        name = "John"
        place = "Boston"
        time = "12 noon"

        # Act.
        result = funcs_to_tst.sentence(name, place, time)

        # Assert.
        self.assertNotEqual(result, f'{place} will go to the {name} at {time}.')

    def test_surface_area_cube_returns_150_valid(self):
        # Arrange.
        length = 5
        expected = 150

        # Act.
        surfaceArea = funcs_to_tst.surface_area_cube(length)

        # Assert.
        self.assertEqual(surfaceArea, expected)

    def test_surface_area_cube_returns_140_invalid(self):
        # Arrange.
        length = 5
        expected = 140

        # Act.
        surfaceArea = funcs_to_tst.surface_area_cube(length)

        # Assert.
        self.assertNotEqual(surfaceArea, expected)

    def test_volume_cube_returns_125_valid(self):
        # Arrange.
        length = 5
        expected = 125

        # Act.
        volume = funcs_to_tst.volume_cube(length)

        # Assert.
        self.assertEqual(volume, expected)

    def test_surface_area_cube_returns_120_invalid(self):
        # Arrange.
        length = 5
        expected = 120

        # Act.
        volume = funcs_to_tst.volume_cube(length)

        # Assert.
        self.assertNotEqual(volume, expected)

    def test_registration_returns_tuple_name_age(self):
        # Arrange.
        name = "Mary"
        age = 27
        expected = (name, age)

        # Act.
        result = funcs_to_tst.registration(name, age)

        # Assert.
        self.assertEqual(result, expected)

    def test_registration_returns_tuple_age_name_invalid(self):
        # Arrange.
        name = "Mary"
        age = 27
        expected = (age, name)

        # Act.
        result = funcs_to_tst.registration(name, age)

        # Assert.
        self.assertNotEqual(result, expected)

    def test_registration_returns_string(self):
        # Arrange.
        name = "Mary"
        age = 15
        expected = 'Not old enough to register!'

        # Act.
        result = funcs_to_tst.registration(name, age)

        # Assert.
        self.assertEqual(result, expected)

    # def test_registration_returns_age_returns_tuple_invalid(self):
    #     # Arrange.
    #     name = "Mary"
    #     age = 15
    #     expected = (name, age)

    #     # Act.
    #     result = funcs_to_tst.registration(name, age)

    #     # Assert.
    #     self.assertNotEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
