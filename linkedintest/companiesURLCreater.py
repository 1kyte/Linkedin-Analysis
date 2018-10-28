import re, time, json,csv

def openFile():
    page = 1
    companyData = []
    try:
        while page<4:
            with open("collectionBox/australiaCompanies/companyInfo/auCompanies"+str(page)+".json",'r') as f:
                data = json.load(f)

                companyData+=data
                page +=1

        # print companyData



    except IOError,message:
        print message
    finally:
        f.close()

    try:
        with open("collectionBox/australiaCompanies/companyInfo/comInfo.json", "w") as f2:
                json.dump(companyData, f2)
    except IOError, e:
        print page, e
    finally:
        print ("finish page", page)
        f2.close()

# def filteData(companyData):



if __name__ == "__main__":
    openFile()