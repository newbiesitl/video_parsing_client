import requests
from src.client_config import DETECT_CAR_ENDPOINT_PREFIX
def detect_car_give_ts(ts):
    url = DETECT_CAR_ENDPOINT_PREFIX+str(ts)
    print(url)
    r = requests.get(url)
    return r.content