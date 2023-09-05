import requests
import logging
from jsonschema import validate


logger = logging.getLogger('api')


class Post:
    def __init__(self, url):
        self.url = url

    POST_CREATE = "api/users"

    def create_user(self, body: dict, schema: dict):
        response = requests.post(f'{self.url}{self.POST_CREATE}', json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return response

