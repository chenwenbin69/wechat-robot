# -*- coding:utf-8 -*-

__author__ = 'wenbin'

from wxpy import *
from tuling import ai_search_V1,ai_search_V2


# tuling = Tuling(api_key=constants.TULING_TOKEN)

bot = Bot(cache_path=True)
bot.enable_puid()

myfriend = bot.friends().search('羊')[0]
puid = myfriend.puid

# @bot.register(myfriend)
# def reply_myfriend(msg):
#
#     if '嗨' in msg.text:
#
#         reply_msg = ai_search_V1(msg=msg.text[1:],puid=puid)
#         msg.reply(reply_msg)
#


@bot.register(myfriend)
def reply_myfriend(msg):

    if '嗨' in msg.text:

        reply_msg = ai_search_V2(msg=msg.text[1:],puid=puid)
        msg.reply(reply_msg)


embed()


