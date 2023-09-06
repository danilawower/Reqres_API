from api.api import Delete


URL = "https://reqres.in/"


class TestDelete:

    def test_delete(self):
        response = Delete(url=URL).delete()
        assert response.status_code == 204

