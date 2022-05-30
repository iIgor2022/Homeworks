import requests
import os
from pprint import pprint


class YandexUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_headers(self):
        return {"Accept": "application/json",
                "Authorization": "OAuth {}".format(self.token)}

    def _get_upload_link(self, file_name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self._get_headers()
        params = {"path": {file_name}, "overwrite": "true"};
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path):
        if not os.path.isfile(file_path):
            print(f"Файл {file_path} не найден")
            return
        file_name = os.path.split(file_path)[1]
        href = self._get_upload_link(file_name).get("href", "")
        response = requests.put(href, data=open(file_path, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == "__main__":
    path_to_file = input("Укажите полный путь до файла: ")
    token = input("Введите ваш токен: ")
    uploader = YandexUploader(token)
    uploader.upload(path_to_file)