from django.test import TestCase
from django.test import Client

class PageViewTests(TestCase):

    c = Client()

    def test_page_status_code(self):
        response = self.c.get('/location/beachs')
        self.assertEquals(response.status_code, 200)