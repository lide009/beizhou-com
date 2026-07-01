import urllib.request
import os

logo_urls = [
    ('https://upload.wikimedia.org/wikipedia/zh/8/80/Peking_University_Logo.png', 'pku-logo.png'),
    ('https://upload.wikimedia.org/wikipedia/commons/6/6d/Kyoto_University_emblem.png', 'kyoto-logo.png'),
    ('https://upload.wikimedia.org/wikipedia/zh/2/2c/%E5%8C%97%E4%BA%AC%E5%B8%88%E8%8C%83%E5%A4%A7%E5%AD%A6%E6%A0%A1%E5%BE%BD.png', 'bnu-logo.png'),
]

public_dir = r'd:\trae工作路径\beizhou-full\public'

for url, filename in logo_urls:
    try:
        filepath = os.path.join(public_dir, filename)
        urllib.request.urlretrieve(url, filepath)
        if os.path.exists(filepath):
            print(f'Success: {filename} ({os.path.getsize(filepath)} bytes)')
        else:
            print(f'Failed: {filename}')
    except Exception as e:
        print(f'Error downloading {filename