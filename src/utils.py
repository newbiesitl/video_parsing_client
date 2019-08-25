import requests

from src.image_utils import download_image
from src.client_config import DETECT_CAR_ENDPOINT_PREFIX, IS_SAME_CAR_ENDPOINT_PREFIX


def detect_car_give_ts(ts):
    url = DETECT_CAR_ENDPOINT_PREFIX+str(ts)
    r = requests.get(url)
    return r.json()


def is_match(ts1, ts2):
    url = IS_SAME_CAR_ENDPOINT_PREFIX+'timeStamp1=%s&timeStamp2=%s' % (ts1, ts2)
    r = requests.get(url)
    return r.json()


def analyze(ts1, ts2):
    if ts2 < ts1:
        return 'end time %d should be greater than start time %d' % (ts2, ts1)
    diff = ts2-ts1
    step_size = max(diff//100, 1)
    cur_ts = ts1
    car_left_b = None
    last_car_end = None
    car_right_b = None
    while cur_ts <= ts2:
        is_car_ret = detect_car_give_ts(cur_ts)
        if is_car_ret['status'] == 'error':
            cur_ts += step_size
            continue

        if detect_car_give_ts(cur_ts)['result'].lower() == 'true': #and is_prev_frame_car == 'false':
            reference_ts = cur_ts
            car_right_b = cur_ts
            if car_left_b is None:
                car_left_b = reference_ts
            if last_car_end is not None and reference_ts > last_car_end + 1:
                print('car parked from %d to %d' % (car_left_b, last_car_end))
                print('download image of %d and %d' % (car_left_b, last_car_end))
                download_image(car_left_b)
                download_image(last_car_end)
                car_left_b = reference_ts
            # run binary search here
            l = cur_ts
            r = ts2
            m = (l+r)//2
            while l < m:
                # print(l, r)
                reference_with_prev = is_match(reference_ts, m-1)
                reference_with_cur = is_match(reference_ts, m)
                if reference_with_prev['status'] == 'error':
                    print(reference_with_prev)
                    break
                if reference_with_cur['status'] == 'error':
                    print(reference_with_cur)
                    break
                if reference_with_prev['result'].lower() == 'true' and reference_with_cur['result'].lower() == 'false':
                    car_right_b = cur_ts
                    break
                elif reference_with_prev['result'].lower() == 'true' and reference_with_cur['result'].lower() == 'true':
                    l = m
                elif reference_with_prev['result'].lower() == 'false' and reference_with_cur['result'].lower() == 'true':
                    l = m
                elif reference_with_prev['result'].lower() == 'false' and reference_with_cur['result'].lower() == 'false':
                    r = m

                m = (l+r)//2
            cur_ts = m+1
            # print('processing %.0f%s \r' % ((cur_ts - ts1) / (ts2 - ts1) * 100, '%'))
            last_car_end = m

        else:
            cur_ts += step_size
            # print('processing %.0f%s \r' % ((cur_ts-ts1)/(ts2-ts1) * 100, '%'))
    if car_left_b is not None and car_left_b < car_right_b:
        print('car parked from %d to %d' % (car_left_b, last_car_end))
        print('download image of %d and %d' % (car_left_b, last_car_end))
        download_image(car_left_b)
        download_image(last_car_end)

if __name__ == "__main__":
    ts1, ts2 = 1538087970, 1538097972
    ts1, ts2 = 1538076003, 1538079781
    analyze(ts1, ts2)
