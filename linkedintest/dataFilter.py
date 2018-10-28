import json,re
from operator import itemgetter

def start():
    readTxtFile()

def readTxtFile():

    try:
        with open("collectionBox/australiaCompanies/companyInfo/compAU_industry.txt", 'r') as f:
            line = f.readlines()

        # l.reverse()
        newList = []
        for key in line:
            k = eval(key)
            dic = {}
            item, num = k
            # if not 'India' in item:
            #     itemList = item.split(',')
            #     item = itemList[0]
            #     if not item == "Australia":
            #         if not item in checkList :
            #             dic["name"] = item
            #             checkList.append(item)
            #             dic["value"] = num
            #             newList.append(dic)
            #         else:
            #             newList = combine(item, num, newList)
            dic["name"] = item
            dic["value"] = num
            newList.append(dic)

        # rows_by_fname = sorted(newList, key=itemgetter('name'))
        rows_by_uid = sorted(newList, key=itemgetter('value'))
        rows_by_uid.reverse()

        with open('collectionBox/australiaCompanies/companyInfo/compAU_industry.json','w') as f2:
            json.dump(rows_by_uid, f2)


    except IOError,message:
        print message
    # finally:
        if f:
            f.close()
        # if f2:
        #     f2.close()



def combineinCity(city,value,itemList):
    for i in itemList:
        if city == i['name']:
            i["value"] += value
    return itemList


def combine(item,value,itemList):
    for i in itemList:
        if item == i['name']:
            i["value"]+=value
    return itemList

if __name__ == "__main__":
    start()