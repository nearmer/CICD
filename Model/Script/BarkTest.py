import requests
url = "https://z.zzek.cn/"
headers = {
    'Content-Type': 'application/json; charset=utf-8'
}

data = {
    "body": "Test Bark Server",
    "title": "Test Title",
    "device_key": "",
    "badge": 1,
    "category": "myNotificationCategory",
    "sound": "minuet.caf",
    "icon": "https://github.com/nearmer/CICD/raw/main/Image/CICDBlog.webp",
    "group": "test",
    "url": "https://mritd.com"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

