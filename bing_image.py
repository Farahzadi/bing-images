"""
get images of day from bing and save it
"""

import json
import sys

import requests
from colorama import Fore, init

from utils import get_arguments_dict, get_config, save_content


init(autoreset=True)

def save_image(image_url, dir_path, image_name):
    res = requests.get(image_url)
    with open(f'{dir_path}\\{image_name}', 'wb') as wf:
        wf.write(res.content)
        print(Fore.GREEN + f'saved "{image_name}" in "{dir_path}"')


def main():
    config_path = get_arguments_dict(sys.argv[1:])['config']
    config = get_config(config_path)
    res = requests.get(config.get('remote_url'))
    json_result = res.json().get('images')
    save_content(json.dumps(json_result, indent=2),
                 config.get('output_path'), 'result.json')
    print(Fore.GREEN + f'saved api result in "{config.get("output_path")}" with name "result.json"')

    first = True
    for item in json_result:
        image_name = item['url'].split('/')[-1]
        save_image(f'http://www.bing.com/{item["url"]}', config.get('output_path'), image_name)
        if first:
            save_image(f'http://www.bing.com/{item["url"]}', config.get('output_path'), '_latest.jpg')
            first = False


if __name__ == '__main__':
    main()
