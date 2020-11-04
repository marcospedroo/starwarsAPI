from django.test import TestCase, Client
from planetas.models import Planeta
# from rest_framework.test import Client


class PlanetaTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_can_create_planeta(self):
        response = self.client.post('/planetas/', {"nome": "Dagobah", "clima": "CO", "terreno": "DE"})

        self.assertEqual(response.status_code, 201)

    def test_can_create_two_planets_same_name(self):
        first_try = self.client.post('/planetas/', {"nome": "Dagobah", "clima": "CO", "terreno": "DE"})

        second_try = self.client.post('/planetas/', {"nome": "Dagobah", "clima": "CO", "terreno": "DE"})
        self.assertEqual(second_try.status_code, 400)
        self.assertEqual(second_try.json().get('nome'), ['planeta with this nome already exists.'])

    def test_can_create_planet_wrong_climate(self):
        response = self.client.post('/planetas/', {"nome": "Dagobah", "clima": "CONGELADO", "terreno": "DE"})

        self.assertEqual(response.status_code, 400)
        self.assertIn('is not a valid choice', response.json().get('clima')[0])

    def test_can_create_planet_wrong_terrain(self):
        response = self.client.post('/planetas/', {"nome": "Dagobah", "clima": "CO", "terreno": "DESERTO"})

        self.assertEqual(response.status_code, 400)
        self.assertIn('is not a valid choice', response.json().get('terreno')[0])

    def test_can_create_two_planets_different_names(self):
        first_try = self.client.post('/planetas/', {"nome": "Dagobah", "clima": "CO", "terreno": "DE"})

        second_try = self.client.post('/planetas/', {"nome": "Tatooine", "clima": "CO", "terreno": "DE"})
        self.assertEqual(second_try.status_code, 201)

    def test_can_find_movies_in_planets(self):
        response = self.client.post('/planetas/', {"nome": "Dagobah", "clima": "CO", "terreno": "DE"})

        self.assertEqual(response.status_code, 201)
        self.assertGreater(response.json().get('filmes'), 0)
