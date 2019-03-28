#coding:UTF-8
"""translate from Baidu API"""

import os
import sys
import random

from hashlib import md5
import json
import requests

APP_ID = os.environ["POPCLIP_OPTION_APP_ID"]
APP_KEY = os.environ["POPCLIP_OPTION_APP_KEY"]
API_URL = "https://fanyi-api.baidu.com/api/trans/vip/translate"

def translate(q):
    """translate"""
    salt = str(random.random())
    sign = md5(APP_ID + q + salt + APP_KEY).hexdigest()
    params = {
        "q":        q,
        "from":     "auto",
        "to":       "zh",
        "appid":    APP_ID,
        "salt":     salt,
        "sign":     sign
    }

    r = requests.get(API_URL, params=params)
    res = []
    for _res in r.json()['trans_result']:
        res.append(_res['dst'])
    res = " | ".join(res)
    print res.encode("utf-8")

if __name__ == "__main__":
    ip = os.environ['POPCLIP_TEXT']
    translate(ip)
