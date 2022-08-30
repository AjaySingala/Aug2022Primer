import unittest
import websites

from unittest.mock import patch

class TestWebsites(unittest.TestCase):
    
    def setUp(self):
        self.item1 = websites.Website('Lamp')
        
    def test_website_access(self):
        with patch('websites.requests.get') as mocked_get:
            mocked_get.return_value.ok = True

            product = self.item1.website_access('5')
            mocked_get.assert_called_with('https://website.com/Lamp/5')

            mocked_get.return_value.ok = False

            product = self.item1.website_access('10')
            mocked_get.assert_called_with('https://website.com/Lamp/10')
            self.assertEqual(product, 'Website could not be reached.')

if __name__ == '__main__':
    unittest.main()