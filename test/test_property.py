import unittest
import requests


class TestProperty(unittest.TestCase):

    BASE_URL = 'http://localhost:8100'

    # Obtener resultados por año de construccion
    def get_by_year(self):

        result = requests.get(
            '{0}/property?year=2011'.format(TestProperty.BASE_URL))
        self.assertEqual(result.status_code, 200)
        data = result.json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['data'][0]['year'], 2011)

    # Obtener resultados por estado
    def get_by_status(self):

        result = requests.get(
            '{0}/property?status=3'.format(TestProperty.BASE_URL))
        self.assertEqual(result.status_code, 200)
        data = result.json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['data'][0]['status_id'], 3)

    # Obtener resultados por ciudad
    def get_by_city(self):

        result = requests.get(
            '{0}/property?city=bogota'.format(TestProperty.BASE_URL))
        self.assertEqual(result.status_code, 200)
        data = result.json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['data'][0]['city'], 'bogota')

    # Obtener resultados por año y estado
    def get_by_year_and_status(self):

        result = requests.get(
            '{0}/property?status=3&year=2011'.format(TestProperty.BASE_URL))
        self.assertEqual(result.status_code, 200)
        data = result.json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['data'][0]['year'], 2011)
        self.assertEqual(data['data'][0]['status_id'], 3)

    # Obtener resultados por estado y ciudad
    def get_by_status_and_city(self):

        result = requests.get(
            '{0}/property?status=3&city=bogota'.format(TestProperty.BASE_URL))
        self.assertEqual(result.status_code, 200)
        data = result.json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['data'][0]['city'], 'bogota')
        self.assertEqual(data['data'][0]['status_id'], 3)

    # Obtener resultados por año y ciudad
    def get_by_year_and_city(self):

        result = requests.get(
            '{0}/property?year=2011&city=bogota'.format(TestProperty.BASE_URL))
        self.assertEqual(result.status_code, 200)
        data = result.json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['data'][0]['city'], 'bogota')
        self.assertEqual(data['data'][0]['year'], 2011)

    # Obtener resultados por año, estado y ciudad
    def get_by_status_year_and_city(self):

        result = requests.get(
            '{0}/property?status=4&year=2011&city=bogota'.format(TestProperty.BASE_URL))
        self.assertEqual(result.status_code, 200)
        data = result.json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['data'][0]['status_id'], 4)
        self.assertEqual(data['data'][0]['city'], 'bogota')
        self.assertEqual(data['data'][0]['year'], 2011)


if __name__ == '__main__':
    unittest.main()
