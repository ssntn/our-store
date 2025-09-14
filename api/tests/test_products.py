from django.test import TestCase
from django.urls import reverse
import json

# Currently, run through the following command 'python manage.py test --keepdb'
# Tests use a temp DB (created & destroyed). Use '--keepdb' to reuse it.

class TestProducts(TestCase):

    # Get all products test
    # Current checklist:
    # Status Code, JSON body, Product list is not empty
    def test_product_list(self):
        url = reverse('create_get_product')
        response = self.client.get(url)

        # Checks for status code and if response body is a JSON object
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")

        # Load JSON body
        #data = json.loads(response.content)

        # Checks if list is not empty
        #self.assertTrue(data)