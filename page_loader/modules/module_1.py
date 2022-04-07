import requests
import re


def recoder_filename(url):
    tmp = str.split(url, '://')
    name = re.sub(r'[^A-Za-z0-9]', '-', tmp[1])
    full_name = f'{name}.html'
    return full_name


def download(url, path):
    page = requests.get(url)
    data = page.text
    name = recoder_filename(url)
    full_path = f'{path}/{name}'
    with open(full_path, 'w+') as file:
        file.write(data)
    return full_path
