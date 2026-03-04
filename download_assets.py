import os
import re
import urllib.request
from urllib.parse import urljoin

base_url = "https://photo-advice.jp/mail/lp201304/"
download_dir = "/Users/kinu/Desktop/tmp/lp-photoadvice/"

def download_file(url, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    if not os.path.exists(filepath):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Downloaded: {url} -> {filepath}")
        except Exception as e:
            print(f"Failed: {url} - {e}")

# index.html から画像を検索
html_path = os.path.join(download_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# src="..." 
files_to_download = re.findall(r'src="(img/[^"]+)"', html_content)
files_to_download += re.findall(r'src="(images/[^"]+)"', html_content)
files_to_download += re.findall(r'src="(js/[^"]+)"', html_content)

for file_path in set(files_to_download):
    url = urljoin(base_url, file_path)
    filepath = os.path.join(download_dir, file_path)
    download_file(url, filepath)

# css から画像を検索
css_files = ["css/base.css", "css/lp.css"]
for css_file in css_files:
    css_path = os.path.join(download_dir, css_file)
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()
        
        # url(../img/...)
        bg_urls = re.findall(r'url\(\.\./(img/[^)]+)\)', css_content)
        bg_urls += re.findall(r'url\(\.\./(images/[^)]+)\)', css_content)
        
        # 不要なクォーテーションを削除
        bg_urls = [url.strip('\'"') for url in bg_urls]
        
        for bg_path in set(bg_urls):
            url = urljoin(base_url, bg_path)
            filepath = os.path.join(download_dir, bg_path)
            download_file(url, filepath)

print("Download complete.")
