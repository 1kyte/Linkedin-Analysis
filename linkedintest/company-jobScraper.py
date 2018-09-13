import re, time, json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup

page = 1

def opendrive():
    global page
    try:

        driver = webdriver.Firefox(executable_path = '/Users/PaulaZ/Downloads/geckodriver')
        driver.get("https://www.linkedin.com/?trk=brandpage_baidu_pc-mainlink")
        driver.find_element_by_id('login-email').send_keys("analysisZ@outlook.com")
        driver.find_element_by_id('login-password').send_keys("pa$$w0rd")
        driver.find_element_by_xpath('//*[@id="login-submit"]').click()

    except (NoSuchElementException,WebDriverException), message:
        print message




if __name__ == "__main__":
    opendrive()