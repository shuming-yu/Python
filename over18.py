# Python爬蟲小人生(2) : https://ithelp.ithome.com.tw/articles/10202493
import requests
from bs4 import BeautifulSoup

# r = requests.get('https://www.ptt.cc/bbs/joke/index.html')
# soup = BeautifulSoup(r.text,"html.parser")
# btn = soup.select("div.btn-group.btn-group-paging a")
# url = "https://www.ptt.cc" + btn[1]['href']
# print(url)


payload = {
  "from": "/bbs/Gossiping/index.html",
  "yes": "yes"
}

r = requests.Session()
r1 = r.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html", payload)
r2 = r.get("https://www.ptt.cc/bbs/Gossiping/index.html")
print(r2.text)
