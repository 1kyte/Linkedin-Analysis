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
        while page<11:
            goToTargetPage(driver)

    except (NoSuchElementException,WebDriverException), message:
        print message

    finally:
        driver.close()


def goToTargetPage(driver):
    global page
    try:
        url="https://www.linkedin.com/search/results/companies/?origin=SWITCH_SEARCH_VERTICAL&page="
        driver.get(url+str(page))
        scrollDown(driver)
        getCurrentPageURLs(driver)

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

def getCurrentPageURLs(driver):
    global page
    try:
        bs = BeautifulSoup(driver.page_source, "lxml")
        a = bs.find_all('a', {'class': "search-result__result-link ember-view"})
        getURL(a,driver)
        page += 1
    except (NoSuchElementException,WebDriverException), message:
        print message

def getURL(a,driver):
    urls = []
    head = "https://www.linkedin.com"
    companies = []
    for tagA in a:
        url = re.findall(r'href=.+id', str(tagA))
        u = str(url[0]).strip('href=id\"')
        ur = str(u).strip('\"')
        l = str(ur).replace('\"', '')
        r = str(l).strip(' ')
        temp=head+r+"jobs/"
        if urls ==[]:
            theURL = temp
            urls.append(theURL)
            c = scrapyCompany(theURL, driver)
            companies.append(c)
        else:
            if temp != urls[-1]:
                theURL = temp
                urls.append(theURL)
                c = scrapyCompany(theURL, driver)
                companies.append(c)
    try:
        with open("companyData"+str(page)+".json", "w") as f:
            json.dump(companies, f)
    except IOError,e:
        print e
    finally:
        f.close()


def scrapyCompany(theURL,driver):
    companies={}
    driver.get(theURL)
    time.sleep(3)
    name = getCompany(driver)
    companies['name']=name
    companies['bar']={}
    driver.execute_script("window.scrollTo(0,1000);")
    time.sleep(3)
    classList=['org-cultural-insights-jobs-module__insight org-cultural-insights-jobs-module__insight--seniorities org-company-insights__insight insight-container',
               'org-cultural-insights-jobs-module__insight org-cultural-insights-jobs-module__insight--locations org-company-insights__insight insight-container',
               'org-cultural-insights-jobs-module__insight org-cultural-insights-jobs-module__insight--degree-levels org-company-insights__insight insight-container',
               'org-cultural-insights-jobs-module__insight org-cultural-insights-jobs-module__insight--skills org-company-insights__insight insight-container']

    for c in classList:
        bs = BeautifulSoup(driver.page_source, "lxml")
        levelBlock = bs.find_all('div', {
            'class': c})
        title = getTitle(str(levelBlock))
        items = getItem(str(levelBlock))
        companies['bar'][title]=items
    return companies


def getTitle(whereBlock):
    bs = BeautifulSoup(whereBlock, "lxml")
    titleTag = bs.find_all('h4',{'class':'Sans-17px-black-100%'})
    title = re.findall(r'>.*<',str(titleTag[0]))
    title2 = str(title[0]).strip('><')
    return title2


def getItem(whereBlock):
    bs = BeautifulSoup(whereBlock, "lxml")
    itemsTag = bs.find_all('div',{'class':'org-bar-graph-element__percentage-bar-info Sans-15px-black-70%'})
    item=[]
    for tag in itemsTag:
        tagBs = BeautifulSoup(str(tag), "lxml")
        number = tagBs.find_all('strong')
        numberContent = re.findall(r'\d*[,\d*]|[%]',str(number[0]))[0]
        itemNameTag = tagBs.find_all('span',{'class':'org-bar-graph-element__category'})
        itemContent = re.findall(r'>.*<',str(itemNameTag[0]))
        i = str(itemContent[0]).strip('><')
        item.append({'title':i,'number':numberContent+"%"})
    return item


def getCompany(driver):
    try:
        bs = BeautifulSoup(driver.page_source, "lxml")
        companyTag = bs.find_all('h1',{'class':'org-top-card-module__name Sans-26px-black-85%-light'})
        name = re.findall(r'title=\".*\"',str(companyTag[0]))
        companyName = str(name[0]).strip('title=')
        company = str(companyName).strip('"')
        print company
        return company
    except (NoSuchElementException,WebDriverException), message:
        print message


if __name__ == "__main__":
    opendrive()