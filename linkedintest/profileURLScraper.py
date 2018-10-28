import re, time, json,csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
import csv

urlLists = []
got = []
length = 0
page = 2

def opendrive():

    global got,length
    try:

        driver = webdriver.Firefox(executable_path = '/Users/PaulaZ/Downloads/geckodriver')
        driver.get("https://www.linkedin.com/?trk=brandpage_baidu_pc-mainlink")
        driver.find_element_by_id('login-email').send_keys("analysisZ@outlook.com")
        driver.find_element_by_id('login-password').send_keys("pa$$w0rd")
        driver.find_element_by_xpath('//*[@id="login-submit"]').click()

        url = 'https://www.linkedin.com/in/lucinda-dalla-riva-65371685/'

        getToThePage(driver, url)

        got.append(url)
        length+=1

        for u in urlLists:
            for us in u:
                getToThePage(driver, us[0])

    except (NoSuchElementException,WebDriverException), message:
        print message

    finally:
        driver.close()

def checkLocation(obs):
    try:
        locationTag = obs.find_all('h3',{'class':'pv-top-card-section__location t-16 t-black--light t-normal mt1 inline-block'})
        if not locationTag ==[]:
            for l in locationTag:
                l1 = re.findall(r'\n\s*.*\n',str(l))
                l2 = str(l1[0]).strip().strip('\\n\s')
                print l2
                if 'Australia' in l2 or 'au' in l2 or 'AU' in l2 or 'Melbourne' in l2 or 'VIC' in l2 or 'Victoria' in l2 or 'victoria' in l2:
                    return True
                else:
                    return False
        else:
            return True
    except (NoSuchElementException,WebDriverException), message:
        print message


def getToThePage(driver,url):
    try:
        global urlLists,got,length,page
        driver.get(url)
        scrollDown(driver)

        obs = BeautifulSoup(driver.page_source,'lxml')
        urlList = obs.find_all('a',{'class':'pv-browsemap-section__member ember-view'})
        if not urlList == []:
            urls=[]
            for u in urlList:
                u1 = re.findall(r'href=.*/\"',str(u))
                u2 = str(u1[0]).lstrip('href=\"')
                u3 = str(u2).rstrip('\"')
                u4 = 'https://www.linkedin.com'+u3
                inAus = checkLocation(obs)
                if not u4 in got and inAus:
                    urls.append([u4])
                    got.append(u4)
                    print u4

            length+=len(urls)
            print length

            if length>500:
                page+=1
                length=0

            with open("collectionBox/theUrl"+str(page)+".csv", "a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(urls)

            csvfile.close()
            urlLists.append(urls)


    except (NoSuchElementException,WebDriverException), message:
        print message



def scrollDown(driver):
    driver.execute_script("window.scrollTo(0,500);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(500,1000);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(1000,1500);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(1500,2000);")
    time.sleep(3)

# ======================================================================================================================
# Start the system
# ======================================================================================================================

if __name__ == "__main__":
    opendrive()
