# -*- coding: utf-8 -*-
import re
import json as js
import json
f = open('C:\\Users\Kallen\Documents\GitHub\Linkedin-Analysis\extractResult_withCompany.json','r')

content = js.load(f)
list = {}
totalList = {}
result = []
# finalList = {'business': result}
for i in content:
    # list['company'] = i['company']
    # list['industry'] = i['Detail']['industry']
    # print i['business']
    for j in i['business']:
        for k in range(0, len(j['industry'])):
            list['industry'] = j['industry'][k]
            list['company'] = j['company']
            # print list
    # list['jobFunction'] = i['Detail']['jobFunction']
    # list['jobType'] = i['Detail']['jobType']
    # list['level'] = i['Detail']['level']
    # print list
    # print i['general'].keys()
    # if 'skills' in i.keys() and i['skills'] != []:
    #     for j in range(0, len(i['skills'])):
            # print i['skills'][j]
    # for j in i['business']:
            result.append(list)
            list = {}
# print result
company = []
for i in result:
    if i['industry'] == 'ComputerSoftware':
        company.append(i['company'])
# print company


for i in company:
    # if i['industry'] == 'InformationTechnologyandServices':
    #     print i['company']
        if company.count(i) > 0:
            list[i] = result.count(i)
rank = sorted(list.items(), key=lambda item:item[1])
# print list.keys()
for k, v in list.items():
    if k != None:
        print (k)

# with open("jobTitle.json", "a") as f2:
#
#     json.dump(list.keys(), f2)
# # except IOError, e:
# # print page, e
# # finally:
# # print ("finish page", page)
# f2.close()


    # if len(list) == 0:
    #     list[result[0]] = 1
    # else:
    #     # print list
    #     for k, v in list.items():
    #         if result[i] == k:
    #             print list
    #             v += 1
    #             break
    #             # print v
    #         # else:
    #     list[result[i]] = 1
        # print list

        # print "j", i['business'][1]['industry'][j]
        # list[i['business'][1]['industry'][j]] = 0
        # if list == {}:
        #     list[i['business'][1]['industry'][j]] = 1
        #     # print list
        #     # result.append(list)
        # else:
        #     for key, value in list.items():
        #         # print key
        #         if key == i['business'][1]['industry'][j]:
        #             list[key] += 1
        #             print list[key]
        #             print value
        #             # print list
        #         else:
        #             list[i['business'][1]['industry'][j]] = 1
# print list
                # list.update(i['business'][1]['industry'][j])
    # list['industry'] = i['business']['industry']
    # list['jobTitle'] = i['jobTitle']
    # list['industry'] = i["Detail"]['industry']
    # list['jobType'] = i["Detail"]['jobType']
    # list["level"] = i["Detail"]["level"]
# print list


