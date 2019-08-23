import requests
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
    is_prev_frame_car = None
    original_car_frame_ts = None
    last_car_end = None
    while cur_ts < ts2:
        is_car_ret = detect_car_give_ts(cur_ts)
        if is_car_ret['status'] == 'error':
            cur_ts += step_size
            continue

        if is_prev_frame_car is None:
            is_prev_frame_car = detect_car_give_ts(cur_ts)['result'].lower()
            cur_ts += step_size
        elif detect_car_give_ts(cur_ts)['result'].lower() == 'true' and is_prev_frame_car == 'false':
            # print('car detected at %d' % (cur_ts))
            reference_ts = cur_ts
            if original_car_frame_ts is None:
                original_car_frame_ts = reference_ts
            if last_car_end is not None and reference_ts > last_car_end +1:
                print('car parked from %d to %d' % (original_car_frame_ts, last_car_end))
                original_car_frame_ts = reference_ts
            # run binary search here
            l = cur_ts
            r = ts2
            m = (l+r)//2
            while l < m:
                # print(l, r)
                if is_match(reference_ts, m-1)['result'].lower() == 'true' and is_match(reference_ts, m)['result'].lower() == 'false':
                    is_prev_frame_car = 'false'
                    break
                elif is_match(reference_ts, m-1)['result'].lower() == 'true' and is_match(reference_ts, m)['result'].lower() == 'true':
                    l = m
                elif is_match(reference_ts, m-1)['result'].lower() == 'false' and is_match(reference_ts, m)['result'].lower() == 'true':
                    l = m
                elif is_match(reference_ts, m-1)['result'].lower() == 'false' and is_match(reference_ts, m)['result'].lower() == 'false':
                    r = m

                m = (l+r)//2
            cur_ts = m+1
            last_car_end = m
        else:
            cur_ts += step_size


if __name__ == "__main__":
    ts1, ts2 = 1538076003, 1538079781
    analyze(ts1, ts2)
