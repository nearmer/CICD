import requests

import os


# This is the Bark App push the Message

def barMessage(message: str):

    BARK_KEY = "hL9WWJr4o8JjCZb5xj5yDF"


    KEY = os.environ.get("BARK_KEY")
    urlBase = "https://https://z.zzek.cn/"

    url = url = "https://z.zzek.cn/hL9WWJr4o8JjCZb5xj5yDF"
    headers = {
     'Content-Type': 'application/json; charset=utf-8'
    }
    data = {
        "body": "Test Bark Server",
        "title": "Test Title",
        "device_key": "5e655d613d5262bd53d3599bb6ddf4f255aa670b5a1d3d21901353fc4235ac76",
        "badge": 1,
        "category": "myNotificationCategory",
        "sound": "minuet.caf",
        "icon": "https://github.com/nearmer/CICD/raw/main/Image/CICDBlog.webp",
        "group": "test",
        "url": "https://mritd.com"
    }

    response  =  requests.post(url,headers=headers,json=data)
    print(response)
    records = response.json()
    print(records)
    return records


# This is a demo  for Wechat 

def WechatsendAll(message: str):
 
    KEY = os.environ.get("WECHAT_KEY")

       
    urlBase = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key="

    url = urlBase+KEY

    headers = {
        "Content-Type" : "application/json"
    }
    data = {
        "msgtype" : "text",
        "text":{
            "content" : message,
            "mentioned_lsit" : ["all"]
            }
   
    }

    response  =  requests.post(url,headers=headers,json=data)
    records = response.json()
    print(records)
    return records









