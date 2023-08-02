# 儲存檔案
# file = open("data.txt", mode="w")
# file.write("Hello World!!\nGOGOGO!!!")

# file = open("data.txt", mode="w", encoding="utf-8")
# file.write("測試測試!!!")

# file.close()

# 讀取檔案
with open("data.txt", mode="r", encoding="utf-8") as file:
  data = file.read()
  print(data)

# 讀取json格式
import json
with open("config.json", mode="r", encoding="utf-8") as txtJson:
  dataJson = json.load(txtJson)
  print(dataJson)
  print("PlantCode:", dataJson["PLANT_CODE"])

# 複寫json
dataJson["PLANT_CODE"] = "CP65"
with open("config.json", mode="w", encoding="utf-8") as txtJson:
  json.dump(dataJson, txtJson)
  print(dataJson)