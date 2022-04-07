import os
import requests_mock
from page_loader.modules import module_1


def test_module_1_get_file_name():
    url = 'https://ru.hexlet.io/courses'
    right_name = 'ru-hexlet-io-courses.html'
    url = module_1.recoder_filename(url)
    assert url == right_name


def test_module_1_download():
    with requests_mock.Mocker() as mock:
        mock.get('http://testing.com', text='<my html> <a> with cats </a>')
        full_path = module_1.download('http://testing.com', os.getcwd())
    assert full_path == f'{os.getcwd()}/testing-com.html'
    with open('testing-com.html') as file:
        data = file.read()
    assert data == '<my html> <a> with cats </a>'
