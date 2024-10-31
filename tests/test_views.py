from django.test import TestCase, Client

class IndexViewTest(TestCase):
    def test_index(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/')
        # check that index view / is working
        self.assertEqual(response.status_code, 200)

