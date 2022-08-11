from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

def message_box():
    message_box=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
    message=input("enter msg you want to send:")
    message_box.send_keys(message,"\n")

def message_button():
    message_button=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,'svg[aria-label="Messenger"]'))).click()
    search_person=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'svg[aria-label="New Message"]'))).click()
    search_box=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input')))
    user_name=input("enter person name whom you want to send msg:")
    search_box.send_keys(user_name)
    person=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button/span'))).click()
    next_button=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div[2]/div'))).click()


def not_now():
    not_now_button=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button'))).click()
    another_not_now_button=driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    
    
def login_info():
    email_field=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')))
    password_field=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    login_button=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
    user_name="huzaifa512001"
    password="huzaifa512001."
    email_field.send_keys(user_name)
    password_field.send_keys(password)
    login_button.click()

def link(url):
    driver.get(url)

def initialize_driver():
    driver=webdriver.Chrome()
    return driver

def main():
    global driver
    driver=initialize_driver()
    link("https://www.instagram.com/")
    login_info()
    not_now()
    message_button()
    message_box()

if __name__ == "__main__":
    main()