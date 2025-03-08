from api.api import Get
from schemas.get import single_user_schema, single_user_not_found_schema, list_user_schema, list_schema

URL = "https://reqres.in/"


class TestGet:
    def test_single_user(self):
        response = Get(url=URL).single_user(schema=single_user_schema)
        assert response.status_code == 200

    def test_single_user_not_found(self):
        response = Get(url=URL).single_user_not_found(schema=single_user_not_found_schema)
        assert response.status_code == 404

    def test_list_users(self):
        response = Get(url=URL).list_users(schema=list_user_schema)
        assert response.status_code == 200

    def test_list(self):
        response = Get(url=URL).list(schema=list_schema)
        assert response.status_code == 200