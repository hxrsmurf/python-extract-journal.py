import io, os

newJournal = []
updatedJournal = []
end = "March"
originalFile = "03March.txt"
loopFile = "updated" + originalFile + ".txt"
basePath = "C:\\Users\\kvchm\\Downloads\\"
folderPath = basePath + "\\" + end

def extractJournal():
    global startFile
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    if os.path.isfile(basePath + loopFile):
        loopFileSize = os.path.getsize(basePath + loopFile)
        originalFile = loopFile
        if loopFileSize == 0:
            print("Complete")
            os.remove(basePath + loopFile)
            exit() 
        elif loopFileSize > 29077:
            print ("Error!")
            exit()

    with io.open(basePath + originalFile,"r", encoding = "utf-8-sig") as file:
        x = 0  
        for line in file:        
            if line.startswith(end) and x > 0:
                updatedJournal.append(line)
                break
            if line.startswith("\n"):
                x +=1
                if x > 1:
                    line = line.strip()
                    x = 0
            newJournal.append(line)
            if line.startswith(end):
                x +=1
        for line in file:
            updatedJournal.append(line)

    output = str(''.join(newJournal[:1])).strip()
    print(output)

    with io.open(basePath + output + ".txt","w", encoding="utf-8-sig") as file:
        for line in newJournal:
            file.write(line)

    with io.open(basePath + loopFile,"w", encoding="utf-8-sig") as file:
        for line in updatedJournal:
            file.write(line) 

extractJournal()

