
from api.api import Post
from api.models import create
from schemas.post import create_schema

URL = "https://reqres.in/"


class TestPost:
    def test_create(self):
        body = create()
        response = Post(url=URL).create_user(body=body, schema=create_schema)
        assert response.status_code == 201
        assert response.json().get('id')




