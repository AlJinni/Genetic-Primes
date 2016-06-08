import os, shutil

filePath=os.path.dirname(os.path.abspath(__file__))
primeFolder = os.path.join(filePath, "Clone Wars")
bestFiles=[0]*3
bestProgress=[0]*3
dirGens=[]


def bestList(quadratic, score):
    lowestScore = 100000
    lowestIndex = 100000
    for i in xrange(len(bestScoreList)):
        if lowestScore > bestScoreList[i]:
            lowestScore = bestScoreList[i]
            lowestIndex = i
    if score > lowestScore:
        bestProgress[lowestIndex] = score
        bestFiles[lowestIndex] = quadratic
        return (bestFiles)
    return (bestFiles)

def TEST():
    polyStorageList=[0]*5
    bestScoreList=[0]*5

    for direc in os.listdir(filePath, "Progress Storage"):
        fileID=direc[10:-4]
        print fileID
        progCheck=open(fileID,"r").read()
        bestList(fileID, int(progCheck))


def PURGE():
    print ""
    for prime in os.listdir(primeFolder):
        filePath = os.path.join(primeFolder, prime)
        try:
            if os.path.isfile(filePath):
                os.unlink(filePath)
            elif os.path.isdir(filePath): shutil.rmtree(filePath)
        except Exception as e:
            print(e)
