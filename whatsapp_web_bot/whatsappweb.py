from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=None

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=D:\huzaifa\selenium practice\whatsapp_web_bot\session') 

def link(url):  
    driver.get(url)

def initialize_driver():
    driver=webdriver.Chrome(options=options)
    return driver

def main():
    global driver
    driver=initialize_driver()
    link("https://web.whatsapp.com/")

if __name__ == "__main__":
    main()