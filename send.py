#!/usr/bib/python3
# Author: xu jianzhi
# Date: 2022-04-27


import json
import base64
import imgkit
import hashlib
import requests

# fd = open('', 'br')
# fcont = fd.read()
# fmd5 = hashlib.md5(fcont)
# print(fmd5.hexdigest)


pic_path = '/xxxxxxxxxxxxxxx/111.png'
pic_tmp_path = '/xxxxxxxxxxxxxxx/tmp.jpg'

url = webhook = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxxxxxxxxxxxxxxx'


###########   如果发不成，可以考虑把这段弄出来，因为图片格式问题，重新保存可能会解决，一般用不到

# import cv2
# from skimage import io

# image = io.imread(pic_path)
# image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGRA)
# cv2.imencode('.png',image)[1].tofile(pic_tmp_path)

###########   发送图片

# imgkit.from_string('hello world', pic_tmp_path , options={"encoding": "UTF-8", "xvfb": ""})
    
f = open(pic_path, 'br')            ####
# f = open(pic_tmp_path, 'br')      ####
fcont = f.read()
m2 = hashlib.md5(fcont)
md5_val = m2.hexdigest()
base64_data = str(base64.b64encode(fcont), encoding='utf-8')
r = requests.post(url, data=json.dumps({"msgtype":"image", "image":{"base64":base64_data, "md5":md5_val}}))
print(r)


###########   发送文字

headers = {"Content-Type": "application/json"}
body = {"msgtype": "text", "text": {"content": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "mentioned_list": ["2936xxxx"]}}
# r = requests.post(webhook, headers=headers, data=json.dumps(body))
r = requests.post(url, data=json.dumps({
    "msgtype": "text",
    "text":
    {
        "content": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "mentioned_list":
        [
            "2936xxxx"
        ]
    }
}))
print(r)
