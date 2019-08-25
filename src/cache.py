import os
import requests

from src.client_config import CACHE_DIRs

def get_cache_dir():
    for CACHE_DIR in CACHE_DIRs:
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)

    return CACHE_DIRs


def download_file(url, filename):
    '''
    downloads a the contents of the provided url to a local file
    '''
    contents = requests.get(url).content
    with open(filename, 'wb') as f:
        f.write(contents)
