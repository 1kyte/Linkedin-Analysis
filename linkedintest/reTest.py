# import re, time
# from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import WebDriverException
# from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options

#
# li='div class="job-card-search--two-pane jobs-search-results__list--card--viewport-tracking-0 job-card-search job-card-search--column job-card-search pl4 job-card-search--is-active job-card-search--clickable job-card-search--outline-default ember-view" data-control-name="A_jobssearch_job_result_click" data-job-id="785584726" id="ember2612" role="button" tabindex="0"><div class="job-card-search__image-and-sponsored-container"'
# result=re.findall(r'data-job-id="[0-9]*"', li)
# print(result)
# id=re.findall(r'[0-9]*', str(result))
# print(id[15])
#coding=utf-8
# from selenium import webdriver
# import time
# from selenium.webdriver import ActionChains
#
# driver=webdriver.Firefox(executable_path = '/Users/PaulaZ/Downloads/geckodriver')
# driver.get("https://www.toutiao.com/")
# # driver.save_screenshot("d:\\pp\\liu1.png")
# ac=driver.find_element_by_xpath("//ul[@infinite-scroll-disabled]/li[10]")
# ActionChains(driver).move_to_element(ac).perform()
# time.sleep(2)
# driver.save_screenshot("d:\\pp\\liu2.png")
# jobtitletag='<h1 class="jobs-details-top-card__job-title Sans-21px-black-85%-dense">Pre-Sales Solutions Consultant</h1>'
# jobtitle=re.findall(r'>.*<',str(jobtitletag))
# job=str(jobtitle[0]).strip().strip('><')
# print(job)

# t='\nMelbourne,Australia\n'
# # locationcontent=re.findall(r'>.*<',str(t))
# locationcontent = t.strip('\\n')
# print(locationcontent)
# t2='<div class="jobs-description-details pt4 ember-view" id="ember3790"><!-- --> <h3 class="jobs-box__sub-title js-formatted-exp-title">Seniority Level</h3>\n<p class="jobs-box__body js-formatted-exp-body">Associate</p>\n<!-- -->\n<h3 class="jobs-box__sub-title js-formatted-industries-title">Industry</h3>\n<ul class="jobs-box__list jobs-description-details__list js-formatted-industries-list">\n<li class="jobs-box__list-item jobs-description-details__list-item">\n<a class="jobs-description-details__list-item-link ember-view" data-control-name="job_industry_click" href="/jobs/search/?currentJobId=790814607&amp;f_I=4&amp;location=Melbourne%2C%20Australia&amp;locationId=au%3A4900" id="ember3792">              Computer Software\n</a> </li>\n<li class="jobs-box__list-item jobs-description-details__list-item">\n<a class="jobs-description-details__list-item-link ember-view" data-control-name="job_industry_click" href="/jobs/search/?currentJobId=790814607&amp;f_I=96&amp;location=Melbourne%2C%20Australia&amp;locationId=au%3A4900" id="ember3794">              Information Technology and Services\n</a> </li>\n</ul>\n<h3 class="jobs-box__sub-title js-formatted-employment-status-title">Employment Type</h3>\n<p class="jobs-box__body js-formatted-employment-status-body">Full-time</p>\n<h3 class="jobs-box__sub-title js-formatted-job-functions-title">Job Functions</h3>\n<ul class="jobs-box__list jobs-description-details__list js-formatted-job-functions-list">\n<li class="jobs-box__list-item jobs-description-details__list-item">\n<a class="jobs-description-details__list-item-link ember-view" data-control-name="job_function_link" href="/jobs/search/?currentJobId=790814607&amp;f_F=it&amp;location=Melbourne%2C%20Australia&amp;locationId=au%3A4900" id="ember3796">              Information Technology\n</a> </li>\n<li class="jobs-box__list-item jobs-description-details__list-item">\n<a class="jobs-description-details__list-item-link ember-view" data-control-name="job_function_link" href="/jobs/search/?currentJobId=790814607&amp;f_F=prjm&amp;location=Melbourne%2C%20Australia&amp;locationId=au%3A4900" id="ember3798">              Project Management\n</a> </li>\n</ul>\n</div>'
# b=BeautifulSoup(t2,'lxml')
# # print(b)
#
# getleveltag=b.find_all('p',{"class":"jobs-box__body js-formatted-exp-body"})
# getlevel=re.findall(r'>.*<',str(getleveltag[0]))
# level=str(getlevel[0]).strip('><')
# # print(level)
#
# getIndustry=b.find_all('ul',{"class":"jobs-box__list jobs-description-details__list js-formatted-industries-list"})
# industryBs=BeautifulSoup(str(getIndustry),"lxml")
# getlistElement=industryBs.find_all('li',{"class":"jobs-box__list-item jobs-description-details__list-item"})
# industryList=[]
# for e in getlistElement:
#     el = str(e).replace(' ','')
#     ele=re.findall(r'>(\w+)\\n<',str(el))
#     element=str(ele[0]).strip('><\n')
#     industryList.append(element)
# print(el)
#
# getJobType=b.find_all('p',{"class":"jobs-box__body js-formatted-employment-status-body"})
# jobContent=re.findall(r'>.*<',str(getJobType))
# job=str(jobContent[0]).strip('><')
# print(job)


# def testTest():
#     p = returnListTest()
#     print(p)
#
# def returnListTest():
#     path = [1,2,3,4,5]
#     return path

# def goToNextPage(driver,currentstart):
#     time.sleep(1)
#     url ="https://www.linkedin.com/jobs/search/?currentJobId=786572677&location=Melbourne%2C%20Australia&locationId=au%3A4900&start="+str(currentstart)
#     driver.get(url)
#     getClassicalView(driver)
#     getSplitView(driver)
#
# def opendrive():
#     try:
#         driver = webdriver.Firefox(executable_path = '/Users/PaulaZ/Downloads/geckodriver')
#         driver.get("https://www.linkedin.com/?trk=brandpage_baidu_pc-mainlink")
#         driver.find_element_by_id('login-email').send_keys("analysisZ@outlook.com")
#         driver.find_element_by_id('login-password').send_keys("pa$$w0rd")
#         driver.find_element_by_xpath('//*[@id="login-submit"]').click()
#         driver.get("https://www.linkedin.com/jobs/search/?location=Melbourne%2C%20Australia&locationId=au%3A4900")
#     except (NoSuchElementException,WebDriverException), message:
#         print message
#
#     getClassicalView(driver)
#     getSplitView(driver)
#     currentstart = 2
#     page = 2
#
#     while page<5:
#         goToNextPage(driver,currentstart)
#         currentstart+=1
#         page+=1
#
# def getClassicalView(driver):
#     try:
#         telement = driver.find_element_by_xpath(
#             "//div[@class='relative']/div[@class='dropdown jobs-search-dropdown jobs-search-dropdown--view-switcher closed ember-view']/button[@class='dropdown-trigger jobs-search-dropdown__trigger Sans-13px-black-55%-semibold ember-view']")
#         telement.click()
#         listElement = driver.find_element_by_xpath(
#             "//ul[@class='dropdown-options jobs-search-dropdown__dropdown ember-view']/li[@class='jobs-search-dropdown__option']/button[@class='jobs-search-dropdown__option-button jobs-search-dropdown__option-button--single ']")
#         listElement.click()
#     except (NoSuchElementException,WebDriverException), message:
#         print message
#
# def getSplitView(driver):
#     try:
#         telement = driver.find_element_by_xpath(
#             "//div[@class='relative']/div[@class='dropdown jobs-search-dropdown jobs-search-dropdown--view-switcher closed ember-view']/button[@class='dropdown-trigger jobs-search-dropdown__trigger Sans-13px-black-55%-semibold ember-view']")
#         telement.click()
#         listElement = driver.find_element_by_xpath(
#             "//ul[@class='dropdown-options jobs-search-dropdown__dropdown ember-view']/li[@class='jobs-search-dropdown__option']/button[@class='jobs-search-dropdown__option-button jobs-search-dropdown__option-button--split ']")
#         listElement.click()
#     except (NoSuchElementException,WebDriverException), message:
#         print message

def test():
    # display = Display(visible=0, size=(800, 600))
    # display.start()
    # CHROME_PATH = '/usr/bin/google-chrome'
    # CHROMEDRIVER_PATH = '/Users/PaulaZ/Downloads/chromedriver'
    CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
    WINDOW_SIZE = "1920,1080"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    # chrome_options.binary_location = CHROME_PATH

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options)

    driver.get("https://www.baidu.com")
    print(driver.title)
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    print(driver.title)
    driver.quit()

if __name__ == "__main__":
    # opendrive()
    test()