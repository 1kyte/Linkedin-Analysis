import csv
import sys

# reload(sys)
# sys.setdefaultencoding('utf8')
c=open("C:\\Users\Kallen\Documents\GitHub\Linkedin-Analysis\computerscience_info.csv","r", encoding='utf-8') #以rb的方式打开csv文件
read=csv.reader(c)
result = []
list = {}
dic = {}
for line in read:
    # print (line[3])
    if line != '':
        result.append(line[4])
        list = {}

for i in result:
        if result.count(i) > 0:
            list[i] = result.count(i)
rank = sorted(list.items(), key=lambda item:item[1], reverse=True)
# print(rank)
for j in rank:
    dic[j[0]] = j[1]
    # print(j)
print(dic)

c.close()
