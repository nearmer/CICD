import requests
import os


# This is the Bark App push the Message

def barMessage(message: str):

    BARK_KEY = os.environ.get("BARK_KEY")
   
    DEVICE_KEY = os.environ.get("DEVICE_KEY")

    urlBase = "https://https://z.zzek.cn/"

    url = urlBase+BARK_KEY"
    headers = {
     'Content-Type': 'application/json; charset=utf-8'
    }
    data = {
        "title": "Test Title",
        "body": message,      
        "device_key": DEVICE_KEY,
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









