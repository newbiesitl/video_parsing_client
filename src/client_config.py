server_ip = 'http://localhost:5000/'
server_ip = 'http://136.25.41.218:5000/'

GET_IMAGE_ENDPOINT_PREFIX = server_ip+'v1/ask/get_image?ts='

IS_SAME_CAR_ENDPOINT_PREFIX = server_ip+'v1/ask/match?targetObject=car&returnType=json&pValue=10&'

DETECT_CAR_ENDPOINT_PREFIX = server_ip+'v1/ask/contain?returnType=json&timeStamp='

GET_FILE_ENDPOINT_PREFIX = server_ip+'v1/ask/get_file?ts='




import os
cur_dir = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.join(cur_dir, '..',)
print('project root %s' % (project_root))
DATA_FOLDER = os.path.join(project_root, 'cache')
