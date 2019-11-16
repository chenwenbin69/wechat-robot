# -*- coding:utf-8 -*-

__author__ = 'wenbin'

from wxpy import *
from tuling import ai_search_V1,ai_search_V2


# tuling = Tuling(api_key=constants.TULING_TOKEN)

bot = Bot(cache_path=True)
bot.enable_puid()

boring_group = bot.groups().search('6A')[0]
myfriend = bot.friends().search('羊')[0]
puid = myfriend.puid

# @bot.register(myfriend)
# def reply_myfriend(msg):
#
#     if '嗨' in msg.text:
#
#         reply_msg = ai_search_V1(msg=msg.text[1:],puid=puid)
#         msg.reply(reply_msg)



@bot.register(myfriend)
def reply_myfriend(msg):

    if '嗨' in msg.text:

        reply_msg = ai_search_V2(msg=msg.text[1:],puid=puid)
        msg.reply(reply_msg)

@bot.register(Group,TEXT)
def reply_mygroup(msg):

    if msg.is_at:
        print(msg)
        reply_msg = ai_search_V2(msg=msg.text,puid=msg.member.puid)
        msg.reply(reply_msg)
        print(reply_msg)


embed()


