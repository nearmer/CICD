import requests
import xml.etree.ElementTree as ET
import os
xmlUr = 'https://rsshub.baitry.com/bing'
def download_images_from_rss_link(xml_url, save_folder='bing_images'):
    # 下载XML文件
    response = requests.get(xml_url)
    response.raise_for_status()  # 检查是否成功下载
    
    # 解析XML内容
    root = ET.fromstring(response.content)
    
    # 创建保存图片的文件夹
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    # 遍历XML树，查找所有的图片链接
    count = 0
    for item in root.findall('./channel/item'):
        try:
            # 获取<description>元素的文本并提取URL
            description = item.find('description').text
            # 提取src属性的内容
            start_index = description.find('src="') + 5
            end_index = description.find('"', start_index)
            img_url = description[start_index:end_index]
            
            # 下载图片
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                with open(os.path.join(save_folder, f'image_{count}.jpg'), 'wb') as f:
                    f.write(img_response.content)
                print(f"Downloaded image {count + 1} from {img_url}")
                count += 1
        except Exception as e:
            print(f"Could not download image {count + 1}: {e}")

    print("Download completed!")


# 使用示例，替换 'your_xml_url_here' 为实际的XML链接地址
download_images_from_rss_link(xmlUr)
