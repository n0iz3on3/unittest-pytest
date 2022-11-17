import requests
import pytest

TOKEN = '....'

FIXTURES = [
    ('test_folder', 201), # Успешно создан новый объект
    ('-/blabla', 409), # При редактировании объекта возник конфликт
    ('test_folder', 409),  # При редактировании объекта возник конфликт
    ('//test_folder', 404) # Запрошенный объект не был найден
]

def create_folder(folder_name):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {'Authorization': TOKEN}
    params = {'path': folder_name}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code

class TestYaDiskCreateFoldrer():
    @pytest.mark.parametrize("name, result", FIXTURES)
    def test_folder_status_code(self, name, result):
        assert create_folder(name) == result, 'Something went wrong...'
