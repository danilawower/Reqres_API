from api.api import Post
from api.models import create, register_uns, register
from schemas.post import create_schema, register_uns_schema, register_schema


URL = "https://reqres.in/"


class TestPost:
    def test_create(self):
        body = create()
        response = Post(url=URL).create_user(body=body, schema=create_schema)
        assert response.status_code == 201

    def test_register_uns(self):
        body = register_uns()
        response = Post(url=URL).register(body=body, schema=register_uns_schema)
        assert response.status_code == 400

    def test_register_success(self):
        body = register()
        response = Post(url=URL).register(body=body, schema=register_schema)
        assert response.status_code == 200




