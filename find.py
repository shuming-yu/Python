# [Python爬蟲教學]7個Python使用BeautifulSoup開發網頁爬蟲的實用技巧
import requests
from bs4 import BeautifulSoup

r = requests.get("https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")

soup = BeautifulSoup(r.text, "html.parser")
# 只搜尋第一個符合條件的HTML節點，傳入要搜尋的標籤名稱
result = soup.find('h3')
# print(result)

# 搜尋網頁中所有符合條件的HTML節點，傳入要搜尋的HTML標籤名稱
# 由於執行結果可能會搜出許多的HTML內容，所以最後也可以利用limit關鍵字參數(Keyword Argument)限制搜尋的節點數量
result = soup.find_all('h3', itemprop='headline', limit=5)
# print(result)

# 同時搜尋多個HTML標籤，可以將標籤名稱打包成串列(List)
result = soup.find_all(["h3", "p"], limit=6)
print(result)