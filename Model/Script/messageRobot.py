import requests

import os







# This is the Bark App


def barMessage():

    return


os.environ
# This is a demo  for Wechat 


def sendAll(message: str):

    KEY = ""


    
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


sendAll("Hello world")








