import requests

import os

KEY = " "
    
urlBase = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key="

url = urlBase+KEY

headers = {
    "Content-Type" : "application/json"
}
data = {
    "msgtype" : "text",
    "text":{
        "content" : "123",
        "mentioned_lsit" : ["all"]
        }

}

response  =  requests.post(url,headers=headers,json=data)
