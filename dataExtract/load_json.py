import json
page = 1
while page < 101:
    try:
        with open("C:\\Users\Kallen\Documents\GitHub\Linkedin-Analysis\linkedintest\companyData\companyData"+str(page)+".json", 'r', encoding='utf-8') as f:
            data = json.load(f)

    finally:
        if f:
            f.close()

    try:
        with open("company_extract.json", "a") as f2:
            list = {}
            result = []
            totalList = {'json': result}
            for i in data:
                # print(i)
                result.append(i)
            print(result)
            json.dump(totalList, f2)



            # for k in data:
            #     if data[k] != {}:
            #         # print(k)
            #         for i in data[k]:
            #             # print(i)
            #             if data[k][i] != {}:
            #                 list['position'] = k
            #                 if 'Industry' in i:
            #                     list['industry'] = data[k][i]
            #                 # print(data[k][i])
            #                 if 'Top Location' in i:
            #                     list['location'] = data[k][i]
                    # if j in i['Top Location']:
                    # result.append(list)
            #         list = {}
            # for i in result:
            #     if i != {}:
            #         if 'location' in i.keys() and 'industry' in i.keys():
            #             json.dump(i, f2)
            #             print(i)

            # list['location'] = i['general']['location']
            # list['jobs'] = i['jobs']
            # list['school'] = i['schools']
            #     result.append(j)
            # print(result)
            #     list = {}
        # for j in result:
        #     print(j)

        # print(result)

    # except IOError, e:
    #     print (page, e)
    finally:
        print("finish page", page)
        f2.close()

    page += 1
