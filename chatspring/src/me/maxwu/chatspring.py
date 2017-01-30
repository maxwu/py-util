#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'maxwu'


import sys
import itchat, re
from itchat.content import *

reload(sys)
sys.setdefaultencoding('utf-8')


@itchat.msg_register(TEXT)
def text_reply(msg):
    global count
    print "Msg Received from %s: %s" %(msg['FromUserName'], msg['Text'])

    match = re.search(u'\u5e74', msg['Text'])
    if match:
        count += 1
        print "matched!"
        itchat.send("新春快乐,鸡年大吉, No.%d --robot" % count, msg['FromUserName'])


@itchat.msg_register([PICTURE, RECORDING, VIDEO, SHARING])
def other_reply(msg):
    global count
    count += 1
    itchat.send("发啥都是发,鸡年大吉, No.%d --robot" % count, msg['FromUserName'])


if __name__ == "__main__":
    count = 0
    itchat.auto_login()
    itchat.run(debug=True)
# EOF

