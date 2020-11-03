from selenium import webdriver
import time


# This is the path I use
# DRIVER_PATH = '.../Desktop/Scraping/chromedriver 2'
# Put the path for your ChromeDriver here
# CHANGE THE DRIVER PATH
DRIVER_PATH = "/home/kyler/Downloads/chromedriver_linux64/chromedriver"
wd = webdriver.Chrome(executable_path=DRIVER_PATH)

wd.get("https://steamcommunity.com/app/1085660/screenshots/")

for i in range(5):
    time.sleep(3)
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
wd.quit()
