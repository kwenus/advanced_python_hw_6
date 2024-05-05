from sourse_links import *
from yandex_api_links import *
from functions import create_folder, download_upload_file


if __name__ == '__main__':

    create_folder(headers={'Authorization': token},
                  params={'path': 'Klint'})

    download_upload_file(headers={'Authorization': token},
                         params={'url': klint_canvas_1,
                                 'path': 'Klint/klint_1.jpeg'})
