# -*- coding:utf-8 -*-

__author__ = 'wenbin'

import requests
import json
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

    inputText = {
                "text": msg
            }

    userInfo = {
            "apiKey": constants.TULING_TOKEN,
            "userId": puid
        }

    data = {
        "reqType":0,
        "perception": {
            "inputText": inputText
        },
        "userInfo": userInfo
    }

    res = requests.post(constants.TULING_API_V2,data=json.dumps(data)).json()
    return res['results'][0]['values']['text']