# -*- coding:utf-8 -*-

__author__ = 'wenbin'

import requests
import constants

def ai_search_V1(msg,puid):

    data = {
        'key': constants.TULING_TOKEN,
        'info': msg,
        'userid': puid,
    }

    res = requests.post(constants.TULING_API_V1,data=data).json()
    return res['text']


def ai_search_V2(msg,puid):

    data = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": msg
            },
            "inputImage": {
                "url": ""
            },
            "inputMedia": {
                "url": ""
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "信息路"
                }
            }
        },
        "userInfo": {
            "apiKey": constants.TULING_TOKEN,
            "userId": puid
        }
    }

    res = requests.post(constants.TULING_API_V2,data=data).json()

    print(data)
    print(res)

    return res['results'][0]['values']['text']