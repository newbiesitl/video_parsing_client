# Smart parking assistant client
The Smart Parking Assistant counts the parking status for a parking spot using raw video streams.
 
This is a client application. 


# How to use
1. Unzip the file
2. 
```bash
cd cv-assignment-client
docker build -t cv-assignment .
```
3. After building the image, run following commend in terminal to use it:
```bash
# detect a car
docker run --rm cv-assignment detect 1538076003
# detect a car with result save in cache folder
docker run --rm cv-assignment -v $(pwd)/cache:/usr/src/app/cache detect 1538076003
# compare if two frames has the same car
docker run --rm cv-assignment -v $(pwd)/cache:/usr/src/app/cache compare 1539281382 1539281386
# analyze a period of a time
docker run -v $(pwd)/cache:/usr/src/app/cache --rm cv-assignment analyze 1539301045 1539301055 --output result.json
```
you will see following for for analyze the range 1539291382-1539301385 (may take a while)
```text
car parked from 1539292282 to 1539293368
download image of 1539292282 and 1539293368
car parked from 1539293569 to 1539294386
download image of 1539293569 and 1539294386
{'details': 'streaming at time stamp 1539295329 not available', 'status': 'error'}
car parked from 1539294487 to 1539295580
download image of 1539294487 and 1539295580
car parked from 1539299181 to 1539300279
download image of 1539299181 and 1539300279
car parked from 1539300380 to 1539301055
download image of 1539300380 and 1539301055
```
4. add `--result result.json` to dump the results in json format and save in local cache