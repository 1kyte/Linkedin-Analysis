import json

page = 0
while page <7:
        try:
            with open("C:\Users\Kallen\Documents\GitHub\Linkedin-Analysis\linkedintest\\result10\\result"+str(page)+".json", 'r') as f:
                data = json.load(f)
                # print data

        finally:
            if f:
                f.close()

        try:
            with open("extractResult_withCompany.json", "a") as f2:
                list = {}
                result = []
                finalList = {'business': result}
                for i in data["business"]:
                    list['company'] = i['company']
                    list['industry'] = i['Detail']['industry']
                    list['jobFunction'] = i['Detail']['jobFunction']
                    list['jobType'] = i['Detail']['jobType']
                    list['level'] = i['Detail']['level']
                    result.append(list)
                    list = {}
                json.dump(finalList, f2)
        except IOError,e:
            print page,e
        finally:
            print ("finish page",page)
            f2.close()

        page +=1