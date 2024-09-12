import json
import datetime
import os

# 读取 JSON 文件路径
json_file_path = '2.json'

# 记录时间的文件路径
time_file_path = 'last_update_time.txt'

# 读取 JSON 文件，忽略格式错误
try:
    with open(json_file_path, 'r') as f:
        data = json.load(f)
except json.JSONDecodeError:
    data = {}

# 获取当前日期
now = datetime.datetime.now()
current_date = now.strftime("%m%d")

# 定义要替换的网址和对应的新内容
urls_to_replace = [
    ('https://raw.bgithub.xyz/frxz751113/IPTVzb1/main/综合源.txt', f"{current_date}综合源"),
    ('http://wp.wadg.pro/down.php/直播源2.txt', f"{current_date}直播源2"),
    # 添加更多需要替换的网址和新内容对
]

# 遍历 JSON 数据查找并修改特定网址
for item in data:
    if isinstance(item, dict) and 'url' in item:
        for old_url, new_content in urls_to_replace:
            if old_url in item['url']:
                new_url = replace_in_url(item['url'], old_url.split('/')[-1], new_content)
                item['url'] = new_url

def replace_in_url(url, old_part, new_part):
    return url.replace(old_part, new_part)

# 写入修改后的 JSON 文件
with open('2.json', 'w') as f:
    json.dump(data, f, indent=4)

# 更新记录时间的文件
with open(time_file_path, 'w') as time_file:
    time_file.write(current_date)
