import json as js
import json
f = open('compInfo_extract.json','r')

content = js.load(f)
list = {}
totalList = {}
result = []
# finalList = {'business': result}
for i in content:
    # print(i)
    # if 'name' in i:
    #     list['name'] = i['name']
    # if 'location' in i:
        # list['location'] = i['location']
    # if 'size' in i:
    #     list['size'] = i['size']
    if 'industry' in i:
    #     list['industry'] = i['industry']
        result.append(i['industry'])
    # list = {}
    # print(i)
    # if i['json'] != {}:
    #     for j in i['json']:
    #         if j['bar'] != {}:
    #             print(j)
    # if i !={}:
    #     for j in i['json']:
    #         if j['bar'] != {}:
    #             # print(j['bar']['Where we work'])
    #             for k in range(0, len(j['bar']['Where we work'])):
    #                 if 'Australia' in j['bar']['Where we work'][k]['title']:
    #                     # print(i)
    #                     list['location'] = j['bar']['Where we work']
    #                     list['name'] = j['name']
    #                     result.append(list)
    #                     list = {}

    #     if j['school']:
    #         for k in range(0, len(j['school'])):
    #             if 'degree' in j['school'][k]:
                    # print(j['school'][k])
                    # result.append(j['school'][k]['degree'])
                # if 'degreeSpec' in j['school'][k]:
                #     list['degreeSpec'] = j['school'][k]['degreeSpec']

                # list = {}
                # print(result)
            # print(list)
        # print(j['location'])
        # list['location'] = j['location']
    # list['company'] = i['company']
    # list['industry'] = i['Detail']['industry']
    # print i['business']
    # for j in i['general']:
        # for k in range(0, len(j['industry'])):
    # print(i)
    # list['company'] = i['general']['company']
    # print(i)
    # list['location'] = i['general']['location']
    # list['jobs'] = i['jobs']
    # # for j in range(0, len(i['schools'])):
    # #     # print(i['schools'][j]['schoolName'])
    # #     if i['schools'][j] != {}:
    # list['school'] = i['schools']
            # if i['schools'][j].key != {}:
            #     list['degree'] = i['schools'][j]['degree']
        # else:
        #     i['schools'][j] = ''
            # list['school'] = {}

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

    # list = {}
# for i in result:
#     print (i)
# company = []
# for i in result:
#     if i['industry'] == 'ComputerSoftware':
#         company.append(i['company'])
# # print company
#
# #
# with open("compInfo_extract.json", "a") as f2:
for i in result:
    # print(i)
#         json.dump(i, f2)


    # for k in i['json']:
    #     if k['industry'] in temp:
    #         pass
    #     else:
    #         temp = k['industry']
    #         print(i)

    if result.count(i) > 0:
        list[i] = result.count(i)
# print(list)
rank = sorted(list.items(), key=lambda item:item[1], reverse=True)
for i in rank:
    print(i)


# f2.close()

