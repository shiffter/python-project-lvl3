import argparse
import os
import requests
import requests_mock
from page_loader.modules import module_1


def main():
    parser = argparse.ArgumentParser(description='Page downloader')
    parser.add_argument('--output', help='dir for safe file', default=os.getcwd(), type=str)
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    print(module_1.download(args.url, args.output))


if __name__ == '__main__':
    main()
