from api.api import Get
from schemas.get import single_user_schema


URL = "https://reqres.in/"


class TestGet:
    def test_single_user(self):
        response = Get(url=URL).single_user(schema=single_user_schema)
        assert response.status_code == 200
