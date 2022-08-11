from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=D:\huzaifa\selenium practice\whatsapp_web_bot\session') 

def send_message():
    message_box=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
    message=input("enter message:")
    while True: 
        message_box.send_keys(message,"\n")

def search_person():
    search_box=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="side"]/div[1]/div/label/div/div[2]')))
    person_name=input("enter name whom you want to send message:")
    search_box.send_keys(person_name,"\n")
    
def link(url):  
    driver.get(url)

def initialize_driver():
    driver=webdriver.Chrome(options=options)
    return driver

def main():
    global driver
    driver=initialize_driver()
    link("https://web.whatsapp.com/")
    search_person()
    send_message()

if __name__ == "__main__":
    main()