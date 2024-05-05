from unittest_parametrize import ParametrizedTestCase
from unittest_parametrize import parametrize
from functions import *
from yandex_api_links import *


class TestYandexAPI(ParametrizedTestCase):

    # проверка на статус запроса 201 (папка создалась)
    @parametrize(('headers', 'params', 'expected_result'),
                 [({'Authorization': token}, {'path': 'Some_crap'}, 201)])
    def test_status_code_folder_created(self, headers, params, expected_result):
        actual_result = create_folder(headers=headers, params=params)
        self.assertEqual(actual_result.status_code, expected_result)

    # проверка на статус запроса 409 (папка уже существует)
    @parametrize(('headers', 'params', 'expected_result'),
                 [({'Authorization': token}, {'path': 'Some_crap'}, 409)])
    def test_status_code_folder_exist(self, headers, params, expected_result):
        actual_result = create_folder(headers=headers, params=params)
        self.assertEqual(actual_result.status_code, expected_result)

    # проверка, что папка появилась на диске (по названию  папки)
    @parametrize(('headers', 'params', 'expected_result'),
                 [({'Authorization': token}, {'path': 'Some_crap'}, 'Some_crap')])
    def test_folder_exist(self, headers, params, expected_result):
        actual_result = get_information(headers=headers, params=params)
        self.assertEqual(actual_result.json().get('name'), expected_result)
