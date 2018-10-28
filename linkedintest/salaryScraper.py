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
    driver.get("https://www.linkedin.com/salary/explorer?countryCode=au&titleId=34")
    time.sleep(3)
    salaryInformation={}
    character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for cha in character:
        theList = getsearchList(driver,cha)

        for l in theList:
            if "," in l:
                l = l.split(',')[0]

            content = checkContent(driver,l)
            salaryInformation[l] = content
            print salaryInformation

    try:
        with open("salaryInformation2.json", "w") as f2:

            json.dump(salaryInformation, f2)
    except IOError, e:
        print  e
    finally:

        f2.close()


# def gonextCharacter(driver):



def getsearchList(driver,cha):
    searchInput = driver.find_element_by_xpath("//div[@class='salary-explorer ember-view']/section[@id='insights']/div[@class='user-search-input ember-view']/form[@class='user-search-input-container']/div[@class='search-fields-container']/div[@class='typeahead-container input-container input-title']/div[@class='salary-typeahead ember-view']/artdeco-typeahead[@class='ember-view']/div[@class='ember-view']/input[@class='typeahead-title']")
    searchInput.clear()
    searchInput.send_keys(cha)
    time.sleep(2)

    bsObj = BeautifulSoup(driver.page_source, "lxml")
    l = bsObj.find_all('artdeco-typeahead-result',{'class':'typeahead-result ember-view'})
    theList = []
    for ele in l:
        element = getTitle(ele)
        if not element == 'Assistant':
            theList.append(element)
    return theList

def getTitle(ele):
    firstTitle = re.findall(r'>.*',str(ele))
    title = str(firstTitle[0]).strip().strip('>')
    theTitle = str(title).lstrip(' ')
    return theTitle

def checkContent(driver,title):

    searchInput = driver.find_element_by_xpath("//div[@class='salary-explorer ember-view']/section[@id='insights']/div[@class='user-search-input ember-view']/form[@class='user-search-input-container']/div[@class='search-fields-container']/div[@class='typeahead-container input-container input-title']/div[@class='salary-typeahead ember-view']/artdeco-typeahead[@class='ember-view']/div[@class='ember-view']/input[@class='typeahead-title']")
    searchInput.clear()
    searchInput.send_keys(str(title))
    time.sleep(1)

    button = driver.find_element_by_xpath("//div[@class='find-button-container']/div[@class='typeahead-container']/button[@class='search-salary-button']")
    button.click()

    time.sleep(5)
    content = getContent(driver)
    return content


def getContent(driver):
    ab = BeautifulSoup(driver.page_source, "lxml")
    contentList = {}
    try:
        content = ab.find_all('div',{'class':'explorer-type-container no-data-explorer ember-view'})
        if content ==[]:
            scrollDown(driver)
            con = ab.find_all('div', {'class': 'core-content content-section'})
            if len(con)>0:
                c = dataParse(con[0],driver)
                return c
            else:
                return {}
        else:
            return {}
    except (NoSuchElementException,WebDriverException), message:
        print message



def dataParse(tags,driver):
    obs = BeautifulSoup(str(tags),"lxml")
    salaryRangeandMedian = getSalaryRangeandMedian(obs)
    additionalInsight = getAdditionalInsight(driver)
    industry,fs = getIndustry(driver)
    education = getEducation(driver)
    topLocation = getTopLocation(driver)

    data={'Salary Range and Median':salaryRangeandMedian,'Company Size':additionalInsight,'Industry':industry,'Field of Study':fs,
          'Education':education,'Top Location':topLocation}
    return data


def getTopLocation(driver):
    try:
        obs = BeautifulSoup(driver.page_source,'lxml')
        topLocationTableTag = obs.find_all('div',{'class':'TopLocations TopTable ember-view'})

        if len(topLocationTableTag)>0:
            topLocationbs = BeautifulSoup(str(topLocationTableTag[0]),'lxml')
            if not topLocationbs == []:

                row = topLocationbs.find_all('tr',{'class':'FlexibleTable__row ember-view'})
                if len(row)>0:
                    toplocationTable = {}
                    tr = 1
                    for r in row:
                        theRow={}
                        rowTagBs = BeautifulSoup(str(r),'lxml')
                        locationTag = rowTagBs.find_all('a',{'class':'ember-view'})
                        if not locationTag == []:
                            location1 = re.findall(r'>\s*.*\n',str(locationTag[0]))
                            location2 = str(location1[0]).strip().strip('>\\n\s')
                            location3 = str(location2).lstrip(' ')
                            theRow['location'] = location3

                        medianBaseSalary = rowTagBs.find_all('span',{'class':'ttc-CellContent__median__amount'})
                        if not medianBaseSalary == []:
                            med1 = re.findall(r'\n\s*.*\n',str(medianBaseSalary[0]))
                            med2 = str(med1[0]).strip('\n\s')
                            med3 = str(med2).lstrip(' ')
                            theRow['base salary'] = med3


                        range = rowTagBs.find_all('div',{'class':'ttc-CellContent__range'})
                        if not range == []:
                            range1 = re.findall(r'\n\s*.*\n',str(range[0]))
                            range2 = str(range1[0]).strip('\n\s')
                            range3 = str(range2).lstrip(' ')
                            theRow['range'] = range3

                        toplocationTable[tr]=theRow
                        tr+=1
                    return toplocationTable
                else:
                    return {}
            else:
                return {}
        else:
            return {}
    except (NoSuchElementException,WebDriverException), message:
        print message


def getEducation(driver):
    try:
        obs = BeautifulSoup(driver.page_source,'lxml')
        educationLevelList = obs.find_all('div',{'class','teal education-level-section additional-insights-component horizontal-chart-list ember-view'})
        if len(educationLevelList)>0:
            for eList in educationLevelList:
                list = BeautifulSoup(str(eList),'lxml')
                educationList = list.find_all('li')
                if len(educationList)>0:
                    pair={}
                    pa = 1
                    for l in educationList:
                        tag = BeautifulSoup(str(l),'lxml')
                        education = {}
                        if len(tag)>0:

                            salaryTag = tag.find_all('span',{'class':'base-salary'})
                            if len(salaryTag)>0:
                                for sala in salaryTag:
                                    sala1 = re.findall(r'\n\s*.*\n',str(sala))
                                    sala2 = str(sala1[0]).strip().strip('\\n\s')
                                    education['salary'] = sala2

                            educationDegreeTag = tag.find_all('span',{'class':'company-size'})
                            if len(educationDegreeTag)>0:
                                for edu in educationDegreeTag:
                                    edu1 = re.findall(r'\n\s*.*\n',str(edu))
                                    edu2 = str(edu1[0]).strip().strip('\\n\s')
                                    education['education Degree'] = edu2
                        else:
                            return {}
                        pair[pa] = education
                        pa+=1
                    return pair
                else:
                    return {}
        else:
            return {}
    except (NoSuchElementException, WebDriverException), message:
        print message


def getSalaryRangeandMedian(obs):
    try:
        rangeTagList = obs.find_all('div',{'class':'range'})
        if len(rangeTagList)>1:
            ranges=[]
            for rangeTag in rangeTagList:
                rangeT = str(rangeTag).replace(' ', '')
                range = re.findall(r'R.+K',str(rangeT))
                ranges.append(range)

        median = obs.find_all('span',{'class':'median-amount'})
        if len(median)>1:
            medianList = []
            for m in median:
                m1 = str(m).replace(' ','')
                m2 = re.findall(r'A.*',m1)
                medianList.append(m2)
        if len(medianList)==2 and len(rangeTagList)==2:
            return {'basic Salary':{'median':medianList[0],'range':ranges[0]},'total compentation':{'median':medianList[1],'range':ranges[1]}}
        else:
            return {}
    except (NoSuchElementException,WebDriverException), message:
        print message


def getAdditionalInsight(driver):
    try:
        obs = BeautifulSoup(driver.page_source,'lxml')
        insight = obs.find_all('div',{'class':'blue company-size-section additional-insights-component horizontal-chart-list ember-view'})
        if not insight == []:
            CompanySizeWithSalary = getCompanySize(insight[0])
            return CompanySizeWithSalary
        else:
            return {}
    except (NoSuchElementException, WebDriverException), message:
        print message


def getIndustry(driver):
    obs = BeautifulSoup(driver.page_source,'lxml')

    try:
        industryListTag = obs.find_all('div',{'class':'additional-insights-component ordered-analytic-list ember-view'})
        if len(industryListTag) > 0:
            industList = []
            for indus in industryListTag:
                bs = BeautifulSoup(str(indus),'lxml')
                head = bs.find_all('h3')

                if 'Industry' in str(head):
                    li = bs.find_all('li')

                    if len(li)>0:
                        lis = {}
                        a = 1
                        for l in li:
                            list = {}
                            b = BeautifulSoup(str(l),'lxml')
                            industryContent = b.find_all('span',{'class':'display-text'})
                            if len(industryContent) > 0:
                                for industryC in industryContent:
                                    indus1 = re.findall(r'\n\s*.*\n',str(industryC))
                                    indus2 = str(indus1[0]).strip().strip('\\n\s')
                                    indus3 = indus2.lstrip(' ')
                                    if '&amp;' in indus3:
                                        indus3 = indus3.replace('&amp;',',')
                                    list['industry']=indus3

                            base_salart = b.find_all('span',{'class':'base-salary'})
                            if len(base_salart)>0:
                                for base in base_salart:
                                    base1 = re.findall(r'\n\s*.*\n',str(base))
                                    base2 = str(base1[0]).strip().strip('\\n\s')
                                    list['baseSalary'] = base2

                            lis[a] = list
                            a += 1
                        industList.append(lis)
                    else:
                        industList.append({})

                elif 'Field of study' in str(head):
                    FSlist = bs.find_all('li')
                    if len(FSlist)>0:
                        fs = {}
                        f = 1
                        for s in FSlist:
                            fscont={}
                            fsbs = BeautifulSoup(str(s),'lxml')
                            fsContent = fsbs.find_all('span',{'class':'display-text'})
                            if len(fsContent)>0:
                                for fsCon in fsContent:
                                    fsCon1 = re.findall(r'\n\s*.*\n',str(fsCon))
                                    fsCon2 = str(fsCon1[0]).strip().strip('\\n\s')
                                    fscont['Field of study'] = fsCon2

                            fsSalary = fsbs.find_all('span',{'class':'base-salary'})
                            if len(fsSalary)>0:
                                for fss in fsSalary:
                                    fss1 = re.findall(r'\n\s*.*\n',str(fss))
                                    fss2 = str(fss1[0]).strip().strip('\\n\s')
                                    fscont['salary'] = fss2
                            fs[f]=fscont
                            f+=1
                        industList.append(fs)
                    else:
                        industList.append({})
                else:
                    industList.append({})
            if len(industList)==2:
                return industList[0],industList[1]
            elif len(industList)==1:
                if industList[0].has_key('industry'):
                    return industList[0],{}
                else:
                    return {},industList[0]
        else:
            return {},{}

    except (NoSuchElementException, WebDriverException), message:

        print message



def getCompanySize(insight):
    obs = BeautifulSoup(str(insight),'lxml')
    try:
        companySizeList = obs.find_all('ul',{'class':'horizontal-analytic'})
        if not companySizeList == []:
            o = BeautifulSoup(str(companySizeList[0]),'lxml')
            info = o.find_all('div',{'class':'horizontal-analytic-info'})
            if len(info)>0:
                informa = []
                for i in info:
                    smalltaghtml = BeautifulSoup(str(i),'lxml')
                    information = smalltaghtml.find_all('span')
                    salary = getSalary(information)
                    informa.append(salary)
            return informa
        else:
            return {}


    except (NoSuchElementException, WebDriverException), message:

        print message


def getSalary(info):
    try:
        if len(info)>0:
            infom = []
            for i in info:

                # i1 = str(i).replace(' ','')
                i1 = re.findall(r'>\n\s*.*\n',str(i))
                i2 = str(i1[0]).strip().strip(">\n")
                i3 = str(i2).lstrip(' ')
                infom.append(i3)
            return {'Salary':infom[0],'numberofEmploy':infom[1],'explanation':infom[2]}
        else:
            return {}
    except (NoSuchElementException,WebDriverException), message:
        print message



def readJobTitleList():
    try:
        with open("collectionBox/jobTitle.json", 'r') as f:
            data = json.load(f)
            return data
    except IOError,message:
        print message

    finally:
        if f:
            f.close()


def scrollDown(driver):
    driver.execute_script("window.scrollTo(0,500);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(500,1000);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(1000,1500);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(1500,2000);")
    time.sleep(3)

if __name__ == "__main__":
    start()
