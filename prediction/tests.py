from django.urls import reverse
from django.test import TestCase, Client


class PredictViewTests(TestCase):
    def test_method_not_allowed(self):
        response = self.client.get(reverse('predict'))
        self.assertEqual(response.status_code, 405)
        
    def test_empty(self):
        response = self.client.post(reverse('predict'))
        self.assertEqual(response.status_code, 400)

    def test_invalid(self):
        data = {
            'sold_plu_4046' : 'not number',
            'sold_plu_4225' : 6,
            'sold_plu_4770': 8,
            'small_bags': 4,
            'large_bags': 0,
            'xlarge_bags': 0,
            'organic': 'on',
            'region': 'Albany'
        }
        response = self.client.post(reverse('predict'), data)
        self.assertEqual(response.status_code, 400)

    def test_valid(self):
        data = {
            'sold_plu_4046' : 5,
            'sold_plu_4225' : 6,
            'sold_plu_4770': 8,
            'small_bags': 4,
            'large_bags': 0,
            'xlarge_bags': 0,
            'organic': 'on',
            'region': 'Albany'
        }
        response = self.client.post(reverse('predict'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1019")