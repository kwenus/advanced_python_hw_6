import requests
from yandex_api_links import *


def download_file(url, path):
    response_image = requests.get(url)
    with open(path, 'wb') as image:
        image.write(response_image.content)
    return response_image


def create_folder(headers, params):
    response_create_folder = requests.put(url_resourses, headers=headers, params=params)
    return response_create_folder


def get_information(headers, params):
    response_get_information = requests.get(url_resourses, headers=headers, params=params)
    return response_get_information


def upload_file(headers, params, file_path):
    response_upload_link = requests.get(url_for_upload_file, headers=headers, params=params)
    url_for_upload = response_upload_link.json().get('href')
    with open(file_path, 'rb') as image:
        response_upload_file = requests.put(url_for_upload, files={'file': image})
    return response_upload_file.json()


def download_upload_file(headers, params):
    response_download_upload = requests.post(url_for_upload_file, headers=headers, params=params)
    return response_download_upload
