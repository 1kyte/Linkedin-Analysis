import re,json


def start():
    fileCounter = 0
    folderCounter = 2
    try:
        f2 = open("jobInformationCollection.json", "w+")
        while folderCounter<8:
            while fileCounter<41:

                f = open("result"+"0"+str(folderCounter)+"/result" + str(fileCounter) + ".json")
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