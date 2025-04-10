import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#FILE_PATH = os.path.join(os.getcwd(), "drivers", "chromedriver.exe")
file_path = "\\drivers\\chromedriver.exe"
url = https://parabank.parasoft.com/parabank/index.htm


def test01():
    #driver = webdriver.Chrome(executable_path=FILE_PATH)
    driver = webdriver.Chrome(file_path)
    time.sleep(1)
    driver.get(url)
    time.sleep(1)
    about_us_link = driver.find_element(By.LINK_TEXT, "About Us")
    about_us_link.click()
    time.sleep(1)
    print(driver.title)
    time.sleep(1)
    driver.quit()