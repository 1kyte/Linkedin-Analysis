import re,json


def start():
    fileCounter = 1
    folderCounter = 0
    try:
        f2 = open("collectionBox/companyData.json", "w+")
        while folderCounter<1:
            while fileCounter<101:

                # f = open("result"+"0"+str(folderCounter)+"/result" + str(fileCounter) + ".json")
                f = open("companyData/companyData"+str(fileCounter)+".json")
                for line in f:
                    # print line
                    # with open("jobInformationCollection.json", "w") as f2:
                    # json.dump(line, f2)
                    print "write result: "+str(folderCounter)+" page: "+str(fileCounter)
                    f2.write(line)
                if f:
                    f.close()
                fileCounter+=1

            folderCounter+=1
            fileCounter = 0
        f2.close()
    except IOError,m:
        print m
    # finally:
    #     if f2:
    #         f2.close()

        # with open("result02/result" + str(fileCounter) + ".json", 'r') as f:
            # data = json.load(f)
            # print data

# ======================================================================================================================
# Start the system
# ======================================================================================================================

if __name__ == "__main__":
    start()