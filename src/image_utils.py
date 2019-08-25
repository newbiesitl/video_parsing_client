import os

import requests

from src.client_config import GET_IMAGE_ENDPOINT_PREFIX, CACHE_DIRs


def download_image(ts):
    url = GET_IMAGE_ENDPOINT_PREFIX+str(ts)
    r = requests.get(url)
    print(CACHE_DIRs)
    for CACHE_DIR in CACHE_DIRs:
        file_path = os.path.join(CACHE_DIR, str(ts) + '.jpeg')
        f = open(file_path, 'wb+')
        f.write(bytearray(r.content))
        f.close()