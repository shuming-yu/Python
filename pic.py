# [Python爬蟲教學]有效利用Python網頁爬蟲幫你自動化下載圖片 : https://www.learncodewithmike.com/2020/09/download-images-using-python.html
# FLAG有分成幾種(本處只介紹小編常用): r:讀取 w:寫入 b:二進制開檔 a:追加內容
# 變數名稱 = open("檔案名稱",FLAG)
# 開檔變數名稱.read() #讀取
# 開檔變數名稱.write("寫入內容") #寫入
# 開檔變數名稱.close()

# 1 fail
# import requests
# pic=requests.get('https://imgur.dcard.tw/N2k5kV2m.jpg') #圖片網址
# img2 = pic.content #圖片裡的內容
# print(img2)
# pic_out = open('img1.jpg','wb') #img1.png為預存檔的圖片名稱
# pic_out.write(img2) #將get圖片存入img1.png
# pic_out.close() #關閉檔案(很重要)

# 2
from bs4 import BeautifulSoup
import requests
import os
input_image = input("請輸入要下載的圖片：")

response = requests.get(f"https://unsplash.com/s/photos/{input_image}")
soup = BeautifulSoup(response.text, "lxml")

results = soup.find_all("img", {"class": "tB6UZ a5VGX"}, limit=5)
# print(results)
image_links = [result.get("src") for result in results]  # 取得圖片來源連結
# print(image_links)

for index, link in enumerate(image_links):

  if not os.path.exists("images"):
      os.mkdir("images")  # 建立資料夾

  img = requests.get(link)  # 下載圖片

  with open("images\\" + input_image + str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
      file.write(img.content)  # 寫入圖片的二進位碼


# 3
# import requests
# from bs4 import BeautifulSoup
# f = open('file.txt', 'w')
# r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html") #將網頁資料GET下來
# soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
# sel = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
# for s in sel:
#     print(s["href"], s.text)
#     f.write(str(s["href"]) + s.text+"\n")
# f.close()