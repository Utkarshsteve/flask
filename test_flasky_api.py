import unittest
import requests

class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/v1/sanitized/input"
    API_OBJ_WITH_SQL_INJECTION = {
        "payload":"*"
    }
    API_OBJ_WITHOUT_SQL_INJECTION = {
        "payload":"name"
    }

    # GET request to /v1/sanitized/input/ 
    def test_1_get_request(self):
        r = requests.get(self.API_URL)
        self.assertEqual(r.status_code, 200)

    #POST request to /v1/sanitized/input/
    def test_2_post_request_with_sql_injection(self):
        r = requests.post(self.API_URL, json = ApiTest.API_OBJ_WITH_SQL_INJECTION)
        self.assertEqual(r.status_code, 403)

    def test_3_post_request_without_sql_injection(self):
        r = requests.post(self.API_URL, json = ApiTest.API_OBJ_WITHOUT_SQL_INJECTION)
        self.assertEqual(r.status_code, 201)

