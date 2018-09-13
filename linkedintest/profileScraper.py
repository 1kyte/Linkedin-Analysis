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

    openFirstPage(driver)
    time.sleep(1)
    scrollDown(driver)
    getProfileURL(driver)
    while (page<11):
        changePage(driver)
    # driver.close()

def openFirstPage(driver):
    try:
        url = "https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22au%3A4900%22%5D&origin=FACETED_SEARCH&page=" + str(
            page)
        driver.get(url)

    except (NoSuchElementException,WebDriverException), message:
        print message



def scrollDown(driver):
    driver.execute_script("window.scrollTo(0,250);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(250,500);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(500,750);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(750,1000);")
    time.sleep(3)


def getProfileURL(driver):
    try:
        bsObj = BeautifulSoup(driver.page_source, "lxml")
        resultList = bsObj.find_all('li',{"class":"search-result search-result__occluded-item ember-view"})
        urlFilter(driver,resultList)
        # print len(resultList)
    except (NoSuchElementException,WebDriverException), message:
        print message


def urlFilter(driver,resultList):
    global page
    try:
        l = []
        for liElement in resultList:
            bs = BeautifulSoup(str(liElement),"lxml")
            content = bs.find_all('a',{'class':"search-result__result-link ember-view"})
            if not content == []:
                u = filterHelper(content[0])
                l.append(u)
        print l
        page+=1

    except IOError, e:
        print e


def filterHelper(content):
    result = re.findall(r'href=".+/"', str(content))
    url=str(result[0]).strip('href=\"\"')
    return url

def changePage(driver):
    try:
        global page
        url = "https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22au%3A4900%22%5D&origin=FACETED_SEARCH&page=" +str(page)
        driver.get(url)
        time.sleep(1)
        scrollDown(driver)
        getProfileURL(driver)

    except (NoSuchElementException,WebDriverException), message:
        print message



# ======================================================================================================================
# Start the system
# ======================================================================================================================

if __name__ == "__main__":
    opendrive()