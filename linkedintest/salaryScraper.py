import re, time, json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

def start():
    try:

        driver = webdriver.Firefox(executable_path = '/Users/PaulaZ/Downloads/geckodriver')
        driver.get("https://www.linkedin.com/?trk=brandpage_baidu_pc-mainlink")
        driver.find_element_by_id('login-email').send_keys("analysisZ@outlook.com")
        driver.find_element_by_id('login-password').send_keys("pa$$w0rd")
        driver.find_element_by_xpath('//*[@id="login-submit"]').click()

        openPages(driver)
    except (NoSuchElementException,WebDriverException), message:
        print message
    finally:
        driver.close()

def openPages(driver):
    driver.get("https://www.linkedin.com/salary/explorer?countryCode=au&regionCode=4900&titleId=34")
    time.sleep(3)
    # bsObj = BeautifulSoup(driver.page_source, "lxml")
    # print bsObj
    getsearchList(driver)

def getsearchList(driver):
    searchInput = driver.find_element_by_xpath("//div[@class='salary-explorer ember-view']/section[@id='insights']/div[@class='user-search-input ember-view']/form[@class='user-search-input-container']/div[@class='search-fields-container']/div[@class='typeahead-container input-container input-title']/div[@class='salary-typeahead ember-view']/artdeco-typeahead[@class='ember-view']/div[@class='ember-view']/input[@class='typeahead-title']")
    searchInput.clear()
    searchInput.send_keys("a")
    time.sleep(2)

    bsObj = BeautifulSoup(driver.page_source, "lxml")
    l = bsObj.find_all('artdeco-typeahead-result',{'class':'typeahead-result ember-view'})
    for ele in l:
        element = getTitle(ele)
        checkContent(driver, element)


def getTitle(ele):
    element = str(ele).replace(' ','')
    firstTitle = re.findall(r'>.*',str(element))
    title = str(firstTitle[0]).strip().strip('>')
    return title

def checkContent(driver,title):
    searchInput = driver.find_element_by_xpath(
        "//div[@class='salary-explorer ember-view']/section[@id='insights']/div[@class='user-search-input ember-view']/form[@class='user-search-input-container']/div[@class='search-fields-container']/div[@class='typeahead-container input-container input-title']/div[@class='salary-typeahead ember-view']/artdeco-typeahead[@class='ember-view']/div[@class='ember-view']/input[@class='typeahead-title']")
    searchInput.clear()
    searchInput.send_keys(title)
    button  = driver.find_element_by_xpath("//div[@class='find-button-container']/div[@class='typeahead-container']/button[@class='search-salary-button']")
    time.sleep(5)

if __name__ == "__main__":
    start()