from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--disable-notifications")

service = Service('./chromedriver')  # chromedriver的路径
chrome = webdriver.Chrome(service=service, options=options)
chrome.get("https://www.facebook.com/")
