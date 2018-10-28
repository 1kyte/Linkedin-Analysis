import re, json,time
from bs4 import BeautifulSoup

data = {}
def readfile():
    page = 0
    while page <7:
        try:
            with open("recording10/recording"+str(page)+".json", 'r') as f:
                data = json.load(f)

        finally:
            if f:
                f.close()

        try:
            with open("result10/result" + str(page) + ".json", "w") as f2:
                for job in data:
                    for jobId, content in job.items():
                        jobInformation = informationParse(jobId,content)
                        json.dump(jobInformation, f2)
        except IOError,e:
            print page,e
        finally:
            print ("finish page",page)
            f2.close()

        page +=1
        # time.sleep(100)

# def writeToJsonFile(jobInformation,page):
#     try:
#         with open("record"+str(page)+".json", "w") as f:
#             json.dump(jobInformation, f)
#     except IOError,e:
#         print e

def informationParse(jobId,content):

    bs = BeautifulSoup(str(content), "lxml")
    job = getjob(bs)
    company = getcompany(bs)
    location = getlocation(bs)
    jobDetail =  getJobDetail(bs)
    if len(location)>1:
        jobInformation={"jobId":jobId,"jobTitle":job, "company":company,"location":location[1],"view":location[0],"Detail":jobDetail}
    else:
        jobInformation = {"jobId": jobId, "jobTitle": job, "company": company, "location": "",
                          "view": "", "Detail": jobDetail}
    return jobInformation

def getjob(bs):
    job=""
    try:
        jobtitletag = bs.find_all('h1', {'class': "jobs-details-top-card__job-title t-20 t-black t-normal"})
        jobtitle = re.findall(r'>.*<', str(jobtitletag))
        jo = str(jobtitle[0]).strip().strip('><')
        job = jo.replace('&amp;', ' and ')
        # print job
    except IOError, e :
        print e
    finally:
        return job

def getcompany(bs):
    c = ""
    try:
        companytag = bs.find_all('a', {'class': "jobs-details-top-card__company-url ember-view"})
        getcompany = re.findall(r'>.*<', str(companytag))
        company = str(getcompany[0]).strip().strip('><\\n')
        comp = company.replace(' ', '')
        c = comp.replace('&amp;', ' and ')
    except IOError,e:
        print e
    finally:
        return c

def getViews(viewstag):
    view=""
    try:
        if (viewstag !=""):
            viewsContent = str(viewstag).replace(' ','')
            viewNumber = re.findall(r'n>\\n.*\\n<',str(viewsContent))
            v = str(viewNumber[0]).strip().strip('n><')
            view = str(v).strip('\\n')
            # print view
    finally:
        return view

def getlocation(bs):
    result = []
    try:
        locationtag = bs.find_all('span', {'class': 'jobs-details-top-card__bullet'})
        theLocationtag = ""
        # if(len(locationtag)>1):
        if (str(locationtag[0]).find('views') < 0):
            view = getViews(str(locationtag[1]))
        else:
            view = ""
        result.append(view)
        theLocationtag = str(locationtag[0])
        if(theLocationtag != ""):
            locationcontent=str(theLocationtag).replace(' ','')
            location=re.findall(r'>\\n.*\\n<', str(locationcontent))
            loc=str(location[0]).strip().strip('><')
            lo = str(loc).strip('\\n')
            l = lo.replace('&amp;', ' and ')
        else:
            l=""
        result.append(l)
    finally:
        return result


def getJobDetail(bs):
    jobDetailTag= bs.find_all('div', {'class': 'jobs-description-details pt4 ember-view'})
    if(jobDetailTag!=[]):
        b = BeautifulSoup(str(jobDetailTag), 'lxml')
        level=getlevel(b)
        industry=getIndustry(b)
        jobType=getJobType(b)
        jobFunctionList = getJobFunction(b)
        jobDetail={"level":level,"industry":industry,"jobType":jobType,"jobFunction":jobFunctionList}
        # print jobDetail
        return jobDetail
    else:
        return ""

def getlevel(b):
    getleveltag = b.find_all('p', {"class": "jobs-box__body js-formatted-exp-body"})
    if(getleveltag!=[]):
        try:
            getlevel = re.findall(r'>.*<', str(getleveltag[0]))
            level = str(getlevel[0]).strip('><')
        finally:
            return level
    else:
        return ""

def getIndustry(b):
    getIndustry = b.find_all('ul',
                             {"class": "jobs-box__list jobs-description-details__list js-formatted-industries-list"})
    industryBs = BeautifulSoup(str(getIndustry), "lxml")
    getlistElement = industryBs.find_all('li', {"class": "jobs-box__list-item jobs-description-details__list-item"})
    if(getlistElement!=[]):
        industryList = []
        try:
            for e in getlistElement:
                el = str(e).replace(' ', '')
                # ele = re.findall(r'id.*>.+\\\\n<', str(el))
                ele = re.findall(r'>.+<', str(el))

                # elem = re.findall(r'>.+\\',str(ele[0]))
                # element = str(elem[0]).strip('>\\\\\\\\\\\\\\\\')
                element = str(ele[0]).strip().strip('><')
                print element
                industryList.append(element)


        finally:
            # print industryList
            return industryList
    else:
        return []

def getJobType(b):
    try:
        getJobType = b.find_all('p', {"class": "jobs-box__body js-formatted-employment-status-body"})
        jobContent = re.findall(r'>.*<', str(getJobType))
        job = str(jobContent[0]).strip('><')
    finally:
        return job

def getJobFunction(b):
    getJobFinction = b.find_all('ul',{"class":"jobs-box__list jobs-description-details__list js-formatted-job-functions-list"})
    jobfunctionlistElement = BeautifulSoup(str(getJobFinction), "lxml")
    functionListTag = jobfunctionlistElement.find_all('li')
    jobFunctionList=[]
    try:
        for element in functionListTag:
            el = str(element).replace(' ', '')
            if(el.find('/') < 0):
                ele = re.findall(r'>(\w+)/(\w+)', str(el))
            else:
                ele = re.findall(r'>(\w+)', str(el))
            # print ele
            # elem = str(ele[0]).strip('><\n')
            jobFunctionList.append(ele[0])
        # print jobFunctionList
    finally:
        return jobFunctionList


if __name__ == "__main__":
    readfile()