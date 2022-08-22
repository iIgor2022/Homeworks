import unittest
import requests

HEADERS = {"Content-Type": "application/json",
           "Authorization": ""}

class TestFunction(unittest.TestCase):
    def setUp(self) -> None:
        """Метод setUp вызывается отдельно для каждой функиии в тесте"""
        token = input('Введите токен: ').strip()
        HEADERS["Authorization"] = f'OAuth {token}'

    def test_create_folder(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": "test_folder"}
        self.assertEqual(requests.put(url, headers=HEADERS, params=params).status_code, 201)

    def test_cwheck_folder(self):
        """Лишняя буква в функции объясняется тем, что, оказывается, функции в тесте вызываются в алфавитном порядке.
        Причем сравнение идет посимвольно пока не будет найдено первое отличие"""
        url = "https://cloud-api.yandex.net/v1/disk/resources/"
        params = {"path": "test_folder"}
        self.assertEqual(requests.get(url, headers=HEADERS, params=params).status_code, 200)
