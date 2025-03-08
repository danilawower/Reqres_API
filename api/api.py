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

    POST_REGISTER = "api/register"

    def register(self, body: dict, schema: dict):
        response = requests.post(f'{self.url}{self.POST_REGISTER}', json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return response

    POST_LOGIN = "api/login"

    def login(self, body: dict, schema: dict):
        response = requests.post(f'{self.url}{self.POST_LOGIN}', json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return response


class Get:

    def __init__(self, url):
        self.url = url

    GET_SINGLE_USER = "api/users/2"

    def single_user(self, schema: dict):
        response = requests.get(f'{self.url}{self.GET_SINGLE_USER}')
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return response

    GET_SINGLE_USER_NOT_FOUND = "api/users/23"

    def single_user_not_found(self, schema: dict):
        response = requests.get(f'{self.url}{self.GET_SINGLE_USER_NOT_FOUND}')
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return response


class Put:

    def __init__(self, url):
        self.url = url

    PUT_UPDATE = "api/users/2"

    def update(self, body: dict, schema: dict):
        response = requests.put(f'{self.url}{self.PUT_UPDATE}', json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return response


class Delete:

    def __init__(self, url):
        self.url = url

    DELETE = "api/users/2"

    def delete(self):
        response = requests.delete(f'{self.url}{self.DELETE}')
        return response
