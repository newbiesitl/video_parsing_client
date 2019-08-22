import requests
from src.client_config import DETECT_CAR_ENDPOINT_PREFIX
def detect_car_give_ts(ts):
    headers = {'Content-type': 'application/json',}
    url = DETECT_CAR_ENDPOINT_PREFIX+str(ts)
    print(url)
    r = requests.get(url, headers=headers)
    return r.content