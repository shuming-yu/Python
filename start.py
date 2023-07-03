# Python爬蟲小人生 : https://ithelp.ithome.com.tw/articles/10202121?sc=hot
import requests
from bs4 import BeautifulSoup

# 將網頁資料GET下來
r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
# print(r.text)

# 將網頁資料以html.parser
soup = BeautifulSoup(r.text,"html.parser")
# 取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
sel = soup.select("div.title a")
# print(sel)
# 將爬下來的文章標題印出來
for s in sel:
  print(s['href'], s.text)