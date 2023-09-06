from api.api import Put
from schemas.put import update_schema
from api.models import update

URL = "https://reqres.in/"


class TestPut:

    def test_update(self):
        body = update()
        response = Put(url=URL).update(body=body, schema=update_schema)
        assert response.status_code == 200
