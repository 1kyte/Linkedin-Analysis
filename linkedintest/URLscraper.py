import re, time, json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


# f = open("out.json", "w")
# jobInformationList=[]
currentstart = 0
page = 0

def goToNextPage(driver):
    time.sleep(1)
    url ="https://www.linkedin.com/jobs/search/?currentJobId=786572677&location=Melbourne%2C%20Australia&locationId=au%3A4900&start="+str(currentstart)
    driver.get(url)
    getClassicalView(driver)
    scrollDown(driver)
    getListofCurrentPage(driver)

def opendrive():
    try:
        driver = webdriver.Firefox(executable_path = '/Users/PaulaZ/Downloads/geckodriver')
        driver.get("https://www.linkedin.com/?trk=brandpage_baidu_pc-mainlink")
        driver.find_element_by_id('login-email').send_keys("analysisZ@outlook.com")
        driver.find_element_by_id('login-password').send_keys("pa$$w0rd")
        driver.find_element_by_xpath('//*[@id="login-submit"]').click()
        # driver.get("https://www.linkedin.com/jobs/search/?location=Melbourne%2C%20Australia&locationId=au%3A4900")
        url = "https://www.linkedin.com/jobs/search/?currentJobId=786572677&location=Melbourne%2C%20Australia&locationId=au%3A4900&start=" + str(
            currentstart)
        driver.get(url)
    except (NoSuchElementException,WebDriverException), message:
        print message

    time.sleep(1)
    getClassicalView(driver)
    scrollDown(driver)
    getListofCurrentPage(driver)


def getClassicalView(driver):
    print "current page is",currentstart
    try:
        telement = driver.find_element_by_xpath(
            "//div[@class='relative']/div[@class='dropdown jobs-search-dropdown jobs-search-dropdown--view-switcher closed ember-view']/button[@class='dropdown-trigger jobs-search-dropdown__trigger Sans-13px-black-55%-semibold ember-view']")
        telement.click()
        listElement = driver.find_element_by_xpath(
            "//ul[@class='dropdown-options jobs-search-dropdown__dropdown ember-view']/li[@class='jobs-search-dropdown__option']/button[@class='jobs-search-dropdown__option-button jobs-search-dropdown__option-button--single ']")
        listElement.click()
    except (NoSuchElementException,WebDriverException), message:
        print message


def getSplitView(driver):
    try:
        telement = driver.find_element_by_xpath(
            "//div[@class='relative']/div[@class='dropdown jobs-search-dropdown jobs-search-dropdown--view-switcher closed ember-view']/button[@class='dropdown-trigger jobs-search-dropdown__trigger Sans-13px-black-55%-semibold ember-view']")
        telement.click()
        listElement = driver.find_element_by_xpath(
            "//ul[@class='dropdown-options jobs-search-dropdown__dropdown ember-view']/li[@class='jobs-search-dropdown__option']/button[@class='jobs-search-dropdown__option-button jobs-search-dropdown__option-button--split ']")
        listElement.click()
    except (NoSuchElementException,WebDriverException), message:
        print message

def scrollDown(driver):
    driver.execute_script("window.scrollTo(0,1250);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(1250,2500);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(2500,3750);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(3750,5000);")
    time.sleep(3)

# ======================================================================================================================
# Get information
# ======================================================================================================================

# def getjob(bs):
#     jobtitletag = bs.find_all('h1', {'class': "jobs-details-top-card__job-title Sans-21px-black-85%-dense"})
#     jobtitle = re.findall(r'>.*<', str(jobtitletag))
#     jo = str(jobtitle[0]).strip().strip('><')
#     job = jo.replace('&amp;', ' and ')
#     # print(jobtitle)
#     return job
#
# def getcompany(bs):
#     companytag = bs.find_all('a', {'class': "jobs-details-top-card__company-url ember-view"})
#     getcompany = re.findall(r'>.*<', str(companytag))
#     company = str(getcompany[0]).strip().strip('><\\n')
#     comp = company.replace(' ', '')
#     c = comp.replace('&amp;', ' and ')
#     return c
#
# def getViews(viewstag):
#     if (viewstag !=""):
#         viewsContent = str(viewstag).replace(' ','')
#         viewNumber = re.findall(r'>\n.*\n<',str(viewsContent))
#         v = str(viewNumber[0]).strip().strip('><')
#         view = str(v).strip('\n')
#         return view
#
# def getlocation(bs):
#     locationtag = bs.find_all('span', {'class': 'jobs-details-top-card__bullet'})
#     theLocationtag = ""
#     result=[]
#     if(len(locationtag)>1):
#         if (str(locationtag[0]).find('views') < 0):
#             theLocationtag = str(locationtag[0])
#             view = getViews(str(locationtag[1]))
#             result.append(view)
#         else:
#             theLocationtag = str(locationtag[1])
#     elif(len(locationtag)==1):
#         theLocationtag = str(locationtag[0])
#     if(theLocationtag != ""):
#         locationcontent=str(theLocationtag).replace(' ','')
#         location=re.findall(r'>\n.*\n<', locationcontent)
#         loc=str(location[0]).strip().strip('><')
#         lo = str(loc).strip('\n')
#         l = lo.replace('&amp;', ' and ')
#         result.append(l)
#     return result
#
# def getJobDetail(bs):
#     jobDetailTag= bs.find_all('div', {'class': 'jobs-description-details pt4 ember-view'})
#     if(jobDetailTag!=[]):
#         b = BeautifulSoup(str(jobDetailTag), 'lxml')
#         level=getlevel(b)
#         industry=getIndustry(b)
#         jobType=getJobType(b)
#         jobFunctionList = getJobFunction(b)
#         jobDetail={"level":level,"industry":industry,"jobType":jobType,"jobFunction":jobFunctionList}
#         return jobDetail
#     else:
#         return ""
#
# def getlevel(b):
#     getleveltag = b.find_all('p', {"class": "jobs-box__body js-formatted-exp-body"})
#     if(getleveltag!=[]):
#         getlevel = re.findall(r'>.*<', str(getleveltag[0]))
#         level = str(getlevel[0]).strip('><')
#         return level
#     else:
#         return ""
#
# def getIndustry(b):
#     getIndustry = b.find_all('ul',
#                              {"class": "jobs-box__list jobs-description-details__list js-formatted-industries-list"})
#     industryBs = BeautifulSoup(str(getIndustry), "lxml")
#     getlistElement = industryBs.find_all('li', {"class": "jobs-box__list-item jobs-description-details__list-item"})
#     if(getlistElement!=[]):
#         industryList = []
#         for e in getlistElement:
#             el = str(e).replace(' ', '')
#             ele = re.findall(r'>(\w+)\\\\n<', str(el))
#             element = str(ele[0]).strip('><\n')
#             industryList.append(element)
#         return industryList
#     else:
#         return []
#
# def getJobType(b):
#     getJobType = b.find_all('p', {"class": "jobs-box__body js-formatted-employment-status-body"})
#     jobContent = re.findall(r'>.*<', str(getJobType))
#     job = str(jobContent[0]).strip('><')
#     return job
#
# def getJobFunction(b):
#     getJobFinction = b.find_all('ul',{"class":"jobs-box__list jobs-description-details__list js-formatted-job-functions-list"})
#     jobfunctionlistElement = BeautifulSoup(str(getJobFinction), "lxml")
#     functionListTag = jobfunctionlistElement.find_all('li')
#     jobFunctionList=[]
#     for element in functionListTag:
#         el = str(element).replace(' ', '')
#         if(el.find('/') < 0):
#             ele = re.findall(r'>(\w+)/(\w+)', str(el))
#             print('1')
#         else:
#             ele = re.findall(r'>(\w+)\\\\n<', str(el))
#             print('2')
#         elem = str(ele[0]).strip('><\n')
#         jobFunctionList.append(elem)
#
#     return jobFunctionList

# def getPremiumInformation(bs):
#     premiumInformationTag=bs.find_all('div',{"class":"jobs-box jobs-box--fadein jobs-premium-applicant-insights container-premium ember-view"})
#     print(premiumInformationTag)
#     return str(premiumInformationTag)

def informationParse(bs):
    # job=getjob(bs)
    # c=getcompany(bs)
    # result=getlocation(bs)
    # jobDetail=getJobDetail(bs)
    # content=""
    try:
        content=bs.find_all('div', {'class': 'job-view-layout jobs-details ember-view'})
    # premiumInformation=getPremiumInformation(bs)
    # jobInformation={'jobTitle':job,'company':c,'location':result[1],'views':result[0],'jobDetail':jobDetail,
    #                 'wholeContentTag':str(content)}
    # jobInformationList.append(content)
    finally:
        return content



def getInformation(driver,newUrl):
    driver.get(newUrl)
    time.sleep(4)
    bsObj = BeautifulSoup(driver.page_source, "lxml")
    content = informationParse(bsObj)
    time.sleep(2)
    return content

def getListofCurrentPage(driver):
    jobInformationList=[]
    global page
    global currentstart
    bsObj = BeautifulSoup(driver.page_source, "lxml")
    l = bsObj.find_all('li', {"class": "occludable-update card-list__item jobs-search-two-pane__search-result-item "
                                       "ember-view"})
    head = "https://www.linkedin.com/jobs/search/?currentJobId="
    tail = "&location=Melbourne%2C%20Australia&locationId=au%3A4900&start=" + str(currentstart)
    getSplitView(driver)

    for t in l:
        id = getData_job_id(t)
        newUrl = head + id + tail
        print(id)
        content = getInformation(driver, newUrl)
        jobInformationList.append({id:str(content)})
        # break

    # print(jobInformationList)
    # print >> f, jobInformationList


    try:
        with open("recording04/record"+str(page)+".json", "w") as f:
            json.dump(jobInformationList, f)
    except IOError,e:
        print e
    finally:
        f.close()
    page += 1

    if(currentstart<1000):
        currentstart= currentstart + 25
        goToNextPage(driver)
    else:
        driver.quit()



def getData_job_id(li):
    idAttribute=re.findall(r'data-job-id="[0-9]*"', str(li))
    id=re.findall(r'[0-9]*', str(idAttribute))
    if len(id)>15:
        theid = id[15]
    return theid

# ======================================================================================================================
# Start the system
# ======================================================================================================================

if __name__ == "__main__":
    opendrive()
