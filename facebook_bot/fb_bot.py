from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument("--disable-infobars")
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

def go_to_post():
    post_link=input("Enter post link:")
    driver.get(post_link)
    
def login_info():
    email_field=driver.find_element_by_xpath('//*[@id="email"]')
    password_field=driver.find_element_by_xpath('//*[@id="pass"]')
    login_button=driver.find_element_by_css_selector('button[data-testid="royal_login_button"]')
    email="03349159978"
    password="huzaifa512001"
    email_field.send_keys(email)
    password_field.send_keys(password)
    login_button.click()

def link(url):
    driver.get(url)

def initialize_driver():
    driver=webdriver.Chrome(chrome_options=option)
    return driver

def main():
    global driver
    driver=initialize_driver()
    link("https://facebook.com")
    login_info()
    go_to_post()

if __name__ == "__main__":
    main()