# -*- coding: utf-8 -*-
# http://open.youtu.qq.com/#/develop/api-ocr-general
# github.com/se4

import os
import time
import random
import hmac
import hashlib
import binascii
import base64
import requests
import json

youtu_app_id = os.environ['OPENSHIFT_ENV_YOUTU_APP_ID']
youtu_secret_id = os.environ['OPENSHIFT_ENV_YOUTU_SECRET_ID']
youtu_secret_key = os.environ['OPENSHIFT_ENV_YOUTU_SECRET_KEY']
youtu_qq = os.environ['OPENSHIFT_ENV_YOUTU_QQ']

def cal_sig():
    timestamp = int(time.time())
    expired = str(timestamp + 2592000)
    rdm = str(random.randint(0, 999999999))
    plain_text = 'a={appid}&k={secret_id}&e={expired}&t={timestamp}&r={rdm}&u={qq}&f='
    plain_text = plain_text.format(appid=youtu_app_id,
                                   secret_id=youtu_secret_id,
                                   timestamp=timestamp,
                                   rdm=rdm, qq=youtu_qq,
                                   expired=expired)
    bin = hmac.new(youtu_secret_key.encode(), plain_text.encode(), hashlib.sha1).hexdigest()
    s = binascii.unhexlify(bin)
    s = s + plain_text.encode('ascii')
    signature = base64.b64encode(s).rstrip().decode()
    return signature

def youtu_get_text(image_url):
    signature = cal_sig()
    headers = {'Host': 'api.youtu.qq.com', 'Content-Type': 'text/json', 'Authorization': signature}
    ##filepath = os.path.abspath(image_path)
    data = {'app_id': youtu_app_id, 'url': image_url}
    ##data['image'] = base64.b64encode(open(image_path, 'rb').read()).rstrip().decode('utf-8')
    resp = requests.post('https://api.youtu.qq.com/youtu/ocrapi/generalocr',
                         data=json.dumps(data),
                         headers=headers)
    resptext = ''
    if 'items' in resp.text:
        ###return resp.content.decode('utf-8')
	parsed_resp = json.loads(resp.content.decode('utf-8'))
        for itemstring in parsed_resp['items']:
		resptext = resptext + itemstring
	return resptext
    else:
        return '0'
