import requests

class Website():

    def __init__(self, item):
        self.item = item

    def website_access(self, quantity):
        response = requests.get(f'https://website.com/{self.item}/{quantity}')
        if response.ok:
            return response.text
        else:
            return 'Website could not be reached.'
