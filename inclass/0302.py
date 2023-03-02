import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://tabelog.com/osaka/rstLst/yakiniku/?vs=1&sa=%E5%A4%A7%E9%98%AA%E5%BA%9C&sk=%25E7%2584%25BC%25E8%2582%2589&lid=hd_search1&svd=20210707&svt=1900&svps=2&hfc=1&RdoCosTp=2&cat_sk=%E7%84%BC%E8%82%89"

res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

data = []

for block in soup.find_all(class_="list-rst"):
  try:
    name = block.find('a').string # 店名
    star = block.find('span', class_="c-rating__val").string # 星等
    night_price = block.find_all(class_="c-rating-v3__val")[0].string # 夜間價格
    day_price = block.find_all(class_="c-rating-v3__val")[1].string # 日間價格
    
    data.append({
        "店名": name,
        "星等": star,
        "日間價格": day_price,
        "夜間價格": night_price
    })
  except:
    pass

df = pd.DataFrame(data)
print(df)