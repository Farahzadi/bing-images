""" utility function which used in project """
import json
import os

import requests
from colorama import init, Fore

init(autoreset=True)


def get_arguments_dict(args):
    """
    :param args: list of string with format like "key=value"
    :type args: list or tuple
    :return: dict with format like {key: value}
    """
    return dict(
        [item.strip('--').split('=') if len(item.split('=')) > 1 else [item.strip('--'), True] for item in args])


def get_config_type(config_path):
    """
    differ path type from sti
    :param config_path: path to config can be url or file path
    :type config_path: str

    :return: str representing config_path type
    """
    if not config_path:
        return None
    if config_path.startswith('https:'):
        return 'https'
    if config_path.startswith('http:'):
        return 'http'
    return 'file'


def get_config(config_path):
    """
    get config type based on config_path
    :param config_path: could be file path or network path like http
    :return: config in dict format
    """
    config_type = get_config_type(config_path)
    if not config_type:
        return None
    if config_type == 'file':
        try:
            return json.load(open(config_path, 'r'))
        except json.decoder.JSONDecodeError:
            print(Fore.RED + f'[*]"{config_path}" content is not in JSON format!')
            return None
        except FileNotFoundError:
            print(Fore.RED + f'[*]"{config_path}" not found!')
            return None
    try:
        return requests.get(config_path).json()
    except json.decoder.JSONDecodeError:
        print(Fore.RED + f'[*]"{config_path}" response is not json')


def save_content(content, dir_path, file_name):
    """
    save content and save it in specified path. if path doesn't exists make it
    :param content: content to be saved
    :param dir_path: path of target directory
    :param file_name: name of file

    :type content: str
    :type dir_path: str
    :type file_name: str

    :return: true if successful
    """
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    with open(f'{dir_path}\\{file_name}', 'w') as output_file:
        output_file.write(content)
